import streamlit as st
import json
from datetime import datetime
from time import sleep

st.set_page_config(page_title="3DRS Dashboard", layout="wide")
st.title("📊 3DRS – Driver Monitoring Dashboard")

LOG_PATH = "drowsy_phone_log.json"

st.markdown("### 🚦 Real-Time Alerts")
placeholder = st.empty()

while True:
    try:
        with open(LOG_PATH, 'r') as f:
            data = json.load(f)
    except Exception:
        data = {"drowsy_count": 0, "phone_count": 0, "last_event": "Waiting for data..."}

    with placeholder.container():
        col1, col2 = st.columns(2)
        col1.metric("😴 Drowsiness Events", data["drowsy_count"])
        col2.metric("📵 Phone Usage Events", data["phone_count"])
        st.markdown(f"🔔 Last Event: `{data['last_event']}`")
        st.markdown(f"🕒 Updated at: `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`")

    sleep(2)
