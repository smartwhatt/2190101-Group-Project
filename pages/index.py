import streamlit as st

with st.columns(3)[1]:
    st.title("Drunklingo")
    st.session_state.messages = []

    if "drunk_status" not in st.session_state:
        st.session_state.drunk_status = []
    if "start_time" not in st.session_state:
        st.session_state.start_time = None
    if st.button("Start Session"):
        st.switch_page("pages/chatting.py")
