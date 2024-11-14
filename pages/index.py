import streamlit as st
import datetime


with st.columns(3)[1]:
    st.title("Drunklingo")

    st.session_state.messages = []

    if "drunk_status" not in st.session_state:
        st.session_state.drunk_status = []
    if "start_time" not in st.session_state:
        st.session_state.start_time = None
    if st.button("Start Session"):
        st.switch_page("pages/in_session.py")

    st.header("Session Setting")

    st.session_state["timer_duration"] = st.number_input(
        "Timer Duration (in minutes)", min_value=1, value=15
    )
    st.session_state["time_until_alert"] = st.number_input(
        "Time Until Alert (in seconds)", min_value=1, value=45
    )
