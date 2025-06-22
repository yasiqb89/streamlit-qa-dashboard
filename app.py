import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="QA Dashboard", layout="wide")
st.title("📦 QA Release Dashboard")

# Load summary
summary_url = "https://yasiqb89.github.io/gh-pages/summary.json"
results_url = "https://yasiqb89.github.io/gh-pages/test_results.json"

try:
    summary_resp = requests.get(summary_url)
    summary_resp.raise_for_status()
    summary = summary_resp.json().get("summary", {})
except Exception as e:
    st.error(f"❌ Could not load summary data.\n\n{e}")
    st.stop()

try:
    results_resp = requests.get(results_url)
    results_resp.raise_for_status()
    test_data = results_resp.json()
    df = pd.DataFrame(test_data)
except Exception as e:
    st.error(f"❌ Could not load test results.\n\n{e}")
    st.stop()

# Top Summary Section
with st.container():
    st.subheader("📊 Summary Overview")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total", summary.get("total", "—"))
    col2.metric("Passed", sum
