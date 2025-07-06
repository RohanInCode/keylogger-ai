import streamlit as st
from keylogger_utils import start_keylogger, process_log_file
from analyzer import analyze_logs

st.set_page_config(page_title="Keylogger AI Dashboard", layout="centered")

st.markdown("# 🔐 Keylogger + AI Analyzer")
st.markdown("Welcome to the **Keylogger AI Dashboard**. This web-based tool records keystrokes, cleans logs, and uses AI to extract keywords — all in one place.")

st.sidebar.title("⚙️ Controls")

if st.sidebar.button("▶️ Start Keylogger (10 sec)"):
    with st.spinner("Recording keystrokes..."):
        start_keylogger(duration=10)
    st.success("✅ Keylogging complete.")

if st.sidebar.button("🧹 Clean Logs"):
    cleaned = process_log_file()
    st.text_area("📄 Reconstructed Typed Text", cleaned, height=300)

if st.sidebar.button("🤖 Run AI Analysis"):
    keywords = analyze_logs()
    st.write("🔍 Top Keywords Detected:")
    st.code(", ".join(keywords))
