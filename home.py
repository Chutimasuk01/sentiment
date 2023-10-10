import json
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.header("การวิเคราะห์ความรู้สึกภาษาไทย")
st.subheader("Chutima Suksamai")
st.image('./image/001.jpg')

