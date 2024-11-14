from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import streamlit as st


def state_to_prompt(state):
    return [
        (
            SystemMessage(message["content"])
            if message["role"] == "system"
            else (
                HumanMessage(message["content"])
                if message["role"] == "user"
                else AIMessage(message["content"])
            )
        )
        for message in state
    ]


def prompt_to_state(prompt):
    return [
        {
            "role": message.type if message.type != "human" else "user",
            "content": message.content,
        }
        for message in prompt
    ]


def reset_state():
    st.session_state.drunk_status = []
    st.session_state.start_time = None
    st.session_state.messages = []
    st.session_state.evaluation = None
