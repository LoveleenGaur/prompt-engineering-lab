import json
import streamlit as st

def show():
    st.title("📁 Prompt Templates")
    st.caption("Reusable prompt examples across management and business domains.")

    with open("data/templates.json", "r", encoding="utf-8") as f:
        templates = json.load(f)

    categories = sorted(set(item["category"] for item in templates))

    col1, col2 = st.columns([2, 1])
    with col1:
        search = st.text_input("Search templates", placeholder="Search by title, category, or description...")
    with col2:
        selected_category = st.selectbox("Filter by category", ["All"] + categories)

    filtered = templates

    if selected_category != "All":
        filtered = [t for t in filtered if t["category"] == selected_category]

    if search.strip():
        q = search.lower()
        filtered = [
            t for t in filtered
            if q in t["title"].lower()
            or q in t["category"].lower()
            or q in t["description"].lower()
            or q in t["template"].lower()
        ]

    st.write(f"**Templates found:** {len(filtered)}")

    for item in filtered:
        with st.expander(f"{item['title']} · {item['category']}"):
            st.write(item["description"])
            st.code(item["template"], language=None)
