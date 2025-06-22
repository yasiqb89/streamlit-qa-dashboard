import streamlit as st
import requests

st.set_page_config(page_title="QA Dashboard", layout="centered")
st.title("📦 QA Release Dashboard")

# Load test summary JSON
summary_url = "https://yasiqb89.github.io/gh-pages/summary.json"

try:
    response = requests.get(summary_url)
    response.raise_for_status()
    summary = response.json().get("summary", {})
except Exception as e:
    st.error(f"Could not load summary data.\n\n{e}")
    st.stop()

# Summary Display
st.subheader("Test Run Summary")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total", summary.get("total", "—"))
col2.metric("Passed", summary.get("passed", "—"))
col3.metric("Failed", summary.get("failed", "—"))
col4.metric("Flaky", summary.get("flaky", "0"))

score = max(0, 100 - summary.get("failed", 0) * 10)
st.success(f"🔎 Confidence Score: **{score}/100**")

st.markdown("---")
st.markdown("[📄 View Full HTML Report](https://yasiqb89.github.io/gh-pages/?sort=result)", unsafe_allow_html=True)
