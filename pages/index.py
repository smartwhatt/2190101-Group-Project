import streamlit as st

st.title("Drunklingo")
if "drunk_status" not in st.session_state:
    st.session_state.drunk_status = []
if st.button("Start Session"):
    st.switch_page("pages/chatting.py")
