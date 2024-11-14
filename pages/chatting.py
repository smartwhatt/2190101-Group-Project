import streamlit as st
from datetime import datetime
from langchain_core.messages import HumanMessage
from utils.helper import state_to_prompt, prompt_to_state
from utils.models import get_chat_model, get_evaluation
import asyncio


async def inactive_tracker():
    while True:
        if (datetime.now() - st.session_state.start_time).seconds > st.session_state[
            "time_until_alert"
        ] and len(st.session_state["messages"]) <= 3:
            st.session_state.start_time = None
            st.switch_page("pages/emergency_alert.py")
        await asyncio.sleep(1)


llm, messages, role = get_chat_model()
st.title(f"Chatting with {role[1]}")
prompt = st.chat_input("You")

if len(st.session_state.messages) == 0:
    st.session_state.messages = prompt_to_state(messages)


# Get the initial time that the page was loaded
if st.session_state.start_time is None:
    st.session_state.start_time = datetime.now()

for message in st.session_state.messages[2:]:
    st.chat_message(message["role"]).markdown(message["content"])


if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages = st.session_state.messages + [
        {"role": "user", "content": prompt}
    ]
    response = llm(state_to_prompt(st.session_state.messages) + [HumanMessage(prompt)])
    st.chat_message("ai").markdown(response.content)
    # st.session_state.messages.append({"role": "ai", "content": response.content})
    st.session_state.messages = st.session_state.messages + [
        {"role": "ai", "content": response.content}
    ]
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

asyncio.run(inactive_tracker())
