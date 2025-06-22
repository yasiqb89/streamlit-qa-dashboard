import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="QA Dashboard", layout="centered")
st.title("📦 QA Release Dashboard")

# Load summary JSON
summary_url = "https://yasiqb89.github.io/gh-pages/summary.json"
results_url = "https://yasiqb89.github.io/gh-pages/test_results.json"

try:
    summary_res = requests.get(summary_url)
    summary_res.raise_for_status()
    summary = summary_res.json().get("summary", {})
except Exception as e:
    st.error(f"❌ Could not load summary.json\n\n{e}")
    st.stop()

try:
    results_res = requests.get(results_url)
    results_res.raise_for_status()
    results = results_res.json()
except Exception as e:
    st.error(f"❌ Could not load test_results.json\n\n{e}")
    st.stop()

# --- Summary Metrics
st.subheader("✅ Test Summary")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total", summary.get("total", "—"))
col2.metric("Passed", summary.get("passed", "—"))
col3.metric("Failed", summary.get("failed", "—"))
col4.metric("Flaky", summary.get("flaky", "—"))

# --- Confidence Score
score = max(0, 100 - summary.get("failed", 0) * 10)
st.success(f"🔎 Confidence Score: **{score}/100**")

# --- Pie Chart
st.subheader("📊 Result Breakdown")
status_counts = {
    "Passed": summary.get("passed", 0),
    "Failed": summary.get("failed", 0),
    "Flaky": summary.get("flaky", 0)
}

fig, ax = plt.subplots()
ax.pie(status_counts.values(), labels=status_counts.keys(), autopct="%1.1f%%", startangle=140)
ax.axis("equal")
st.pyplot(fig)

# --- Test Details Table
st.subheader("🧪 Test Results")
df = pd.DataFrame(results)
st.dataframe(df, use_container_width=True)

# --- Report Links
st.markdown("---")
st.markdown("[📄 View Full HTML Report](https://yasiqb89.github.io/gh-pages/?sort=result)", unsafe_allow_html=True)
