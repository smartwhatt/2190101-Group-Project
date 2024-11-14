import streamlit as st
from utils.helper import reset_state

st.markdown(
    """
<style>
.stAudio { display:none; }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
# Alert
The owner of this device has been inactive for a while. Please check on them.
If you are the owner of this device, and have think that this is a mistake, please dismiss this alert.
"""
)

st.audio("./assets/alarm.mp3", format="audio/mp3", autoplay=True, loop=True)


if st.button("Dismiss"):
    reset_state()
    st.switch_page("pages/index.py")
