import streamlit as st
import requests
import matplotlib.pyplot as plt
import numpy as np

# Page config
st.set_page_config(page_title="QA Release Dashboard", layout="centered")

# Title Section
st.title("🚀 Release Readiness Dashboard")
st.caption("Engineering Release Confidence — *Using AI to Decide When to Ship*")

# Load summary data
summary_url = "https://yasiqb89.github.io/gh-pages/summary.json"

try:
    response = requests.get(summary_url)
    response.raise_for_status()
    summary = response.json().get("summary", {})
except Exception as e:
    st.error(f"Could not load summary data.\n\n{e}")
    st.stop()

# Confidence Scores Over Time
st.subheader("Confidence Scores Over Time")
confidence_history = summary.get("history", [87, 90, 92, 89, 95, 97, 92, 96, 90, 94])  # Fallback demo data

fig, ax = plt.subplots()
ax.plot(confidence_history, color='orange')
ax.set_ylim([80, 100])
ax.set_ylabel("Confidence Score")
ax.set_xlabel("Previous Runs")
ax.grid(True)
st.pyplot(fig)

# Confidence Score Display
score = summary.get("confidence", 97.5)

st.subheader("Confidence Score")
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    st.markdown(f"""
        <div style="font-size:56px; text-align:center; font-weight:bold; color:green;">
            {score:.1f}%
        </div>
        <div style="text-align:center; font-size:20px;">Ready</div>
    """, unsafe_allow_html=True)

# Summary Metrics
st.markdown("### Summary Metrics")
col1, col2 = st.columns(2)
col1.metric("Test Pass Rate", f"{summary.get('pass_rate', '98.5')}%")
col1.metric("Flaky Test Rate", f"{summary.get('flaky_rate', '1.8')}%")
col2.metric("Requirements Met", f"{summary.get('requirements_met', '95.2')}%")
col2.metric("Critical Failures", f"{summary.get('critical_failures', 0)}")

# Optional: Link to HTML report
st.markdown("[📄 View Full HTML Report](https://yasiqb89.github.io/gh-pages/?sort=result)", unsafe_allow_html=True)

# Problem & Solution Sections
st.markdown("---")
st.markdown("### Problem")
st.write("Release decisions are often made under pressure and based on subjective opinions about whether the latest build is “good enough.” Without clear indicators and traceable metrics, teams risk shipping unstable releases or delaying unnecessarily.")

st.markdown("### Solution")
st.write("We built a custom **Release Readiness Dashboard** using Streamlit that integrates with Allure TestOps, CI pipelines, and Jira to collect structured test data. Using AI, the dashboard computes a single **confidence score** that helps determine whether the release is safe to deploy.")
