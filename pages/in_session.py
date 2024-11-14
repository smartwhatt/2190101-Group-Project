import streamlit as st
import asyncio
import datetime

from utils.helper import reset_state


async def time_tracker(timer):
    while True:
        mm = (
            st.session_state.timer_duration * 60
            - (datetime.datetime.now() - st.session_state.start_time).seconds
        )

        if st.session_state.show_timer:
            timer.text(f"Time until next chat: {datetime.timedelta(seconds=mm)}")

        if datetime.datetime.now() - st.session_state.start_time > datetime.timedelta(
            minutes=st.session_state.timer_duration
        ):
            st.session_state.start_time = None
            st.switch_page("pages/chatting.py")

        await asyncio.sleep(1)


with st.columns([1, 5, 1])[1] as col1:
    st.title("Currently in Session")
    if st.session_state.start_time is None:
        st.session_state.start_time = datetime.datetime.now()

    timer = st.empty()

    with st.columns([1, 2, 1])[1] as col2:
        if st.button("End Session", type="secondary"):
            reset_state()
            st.switch_page("pages/index.py")

    asyncio.run(time_tracker(timer))
