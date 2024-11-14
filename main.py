import streamlit as st


if __name__ == "__main__":

    pg = st.navigation(
        [
            st.Page("pages/index.py", title="Drunklingo"),
            st.Page("pages/chatting.py", title="Chatting"),
            st.Page("pages/in_session.py", title="In Session"),
            st.Page("pages/emergency_alert.py", title="Alert"),
        ],
        position="hidden",
    )
    pg.run()
