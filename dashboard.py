import streamlit as st
import json
import os
from datetime import datetime

# Load today's article
log_path = "log.json"
today = datetime.now().strftime("%Y-%m-%d")
entry = {}

if os.path.exists(log_path):
    with open(log_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        entry = data.get(today, {})

# Layout
st.title("📰 The Unplugged AI Agent Dashboard")

if entry:
    st.subheader("Today's Topic")
    st.write(entry.get("topic", "No topic found"))

    st.subheader("Generated Article")
    st.text_area("Article", entry.get("article", "No article found"), height=300)

    st.subheader("Timestamp")
    st.write(entry.get("timestamp", "No timestamp found"))

    # Markdown preview for Beehiiv
    st.subheader("📋 Beehiiv Markdown Preview")
    markdown = f"# {entry['topic']}\n\n{entry['article']}\n\n*Published on {entry['timestamp']}*"
    st.code(markdown, language="markdown")
    st.info("✅ Select and copy the markdown above to paste into Beehiiv.")
else:
    st.warning("No article generated for today yet.")
