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


st.header = ("การวิเคราะห์ความรู้สึกภาษาไทย")
st.subheader("ชุติมา")
st.imge("image")
lot3="https://lottie.host/3d462873-9b5f-4269-88e3-aec72bd823b3/nsnU9gsvXR.json"
lottie3 = load_lottieurl(lot3)
st_lottie(lottie3)

st.balloons()