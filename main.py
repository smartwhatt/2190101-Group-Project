import streamlit as st


if __name__ == "__main__":

    pg = st.navigation(
        [
            st.Page("pages/index.py", title="Drunklingo"),
            st.Page("pages/chatting.py", title="Chatting"),
        ]
    )
    pg.run()
