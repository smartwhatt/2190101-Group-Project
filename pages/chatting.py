import streamlit as st
from langchain_core.messages import HumanMessage

from utils.helper import state_to_prompt, prompt_to_state
from utils.models import get_chat_model, get_evaluation


llm, messages, role = get_chat_model()
st.title(f"Chatting with {role[1]}")
prompt = st.chat_input("You")
st.session_state.messages = prompt_to_state(messages)

for message in st.session_state.messages[2:]:
    st.chat_message(message["role"]).markdown(message["content"])

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = llm(state_to_prompt(st.session_state.messages) + [HumanMessage(prompt)])
    st.chat_message("ai").markdown(response.content)
    st.session_state.messages.append({"role": "ai", "content": response.content})
    result = get_evaluation(
        [
            f'{message["role"]}: {message["content"]}'
            for message in st.session_state.messages[1:]
        ]
    )
    st.session_state.evaluation = result.model_dump()
    print(st.session_state.evaluation)

if (
    len(st.session_state.messages) > 10
    and st.session_state.evaluation["confidence"] > 0.7
):
    st.warning(
        f"Based on the conversation, the model is {st.session_state.evaluation['drunk_level']:.2f} confident you are drunk."
    )
    st.session_state.drunk_status.append(st.session_state.evaluation["drunk_level"])
