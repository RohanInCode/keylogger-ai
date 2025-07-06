import streamlit as st
from clean_log import process_log_file
from analyzer import analyze_logs

st.title("🧠 Keylogger AI Dashboard")

# Process raw logs
text = process_log_file()

st.text_area("Reconstructed Typed Text", text, height=300)

st.subheader("Keyword Analysis:")
analyze_logs()
