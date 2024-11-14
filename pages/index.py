import streamlit as st
import datetime


with st.columns([1, 3, 1])[1]:
    st.title("Drunklingo")

    st.session_state.messages = []

    if "drunk_status" not in st.session_state:
        st.session_state.drunk_status = []
    if "start_time" not in st.session_state:
        st.session_state.start_time = None

    with st.columns([1, 2, 1])[1]:
        if st.button("Start Session"):
            st.switch_page("pages/in_session.py")

    # st.header("Session Setting")
    with st.expander("Session Setting"):

        st.session_state["show_timer"] = st.checkbox("Show Timer", value=True)
        st.session_state["timer_duration"] = st.number_input(
            "Timer Duration (in minutes)", min_value=1, value=15
        )
        st.session_state["time_until_alert"] = st.number_input(
            "Inactive Time Until Alert (in seconds)", min_value=1, value=45
        )
        st.session_state["stop_loss"] = st.slider(
            "Stop Loss (Level of drunk that would sound the alarm)",
            min_value=1,
            max_value=10,
            value=5,
        )
