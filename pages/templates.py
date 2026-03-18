import json
import streamlit as st
from utils.theme import inject_theme, page_header, section_label

CATEGORY_COLORS = {
    "Marketing":            ("#e8b84b", "rgba(232,184,75,0.1)"),
    "Human Resources":      ("#2dd4bf", "rgba(45,212,191,0.1)"),
    "Finance":              ("#4ade80", "rgba(74,222,128,0.1)"),
    "Strategy":             ("#a78bfa", "rgba(167,139,250,0.1)"),
    "Operations":           ("#fb923c", "rgba(251,146,60,0.1)"),
    "Leadership":           ("#f472b6", "rgba(244,114,182,0.1)"),
    "Business Communication": ("#60a5fa", "rgba(96,165,250,0.1)"),
    "Data & Analytics":     ("#34d399", "rgba(52,211,153,0.1)"),
    "Project Management":   ("#f87171", "rgba(248,113,113,0.1)"),
}


def cat_colors(cat: str):
    return CATEGORY_COLORS.get(cat, ("#e8b84b", "rgba(232,184,75,0.1)"))


def show():
    inject_theme()
    page_header("📁", "Prompt Templates",
                "Ready-to-use SHARP-structured prompts across business and management domains.")

    with open("data/templates.json", "r", encoding="utf-8") as f:
        templates = json.load(f)

    categories = sorted(set(item["category"] for item in templates))

    # ── Stats bar ─────────────────────────────────────────────────────────────
    col_s, col_c, col_d = st.columns(3)
    with col_s:
        st.markdown(
            f"""<div class="stat-card">
                <div class="stat-value">{len(templates)}</div>
                <div class="stat-label">Templates</div>
            </div>""",
            unsafe_allow_html=True,
        )
    with col_c:
        st.markdown(
            f"""<div class="stat-card">
                <div class="stat-value">{len(categories)}</div>
                <div class="stat-label">Categories</div>
            </div>""",
            unsafe_allow_html=True,
        )
    with col_d:
        st.markdown(
            """<div class="stat-card">
                <div class="stat-value">5</div>
                <div class="stat-label">SHARP Dims</div>
            </div>""",
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Filters ───────────────────────────────────────────────────────────────
    col1, col2 = st.columns([3, 1])
    with col1:
        search = st.text_input("Search templates", placeholder="Search by title, category, or keywords…")
    with col2:
        sel_cat = st.selectbox("Category", ["All"] + categories)

    filtered = templates
    if sel_cat != "All":
        filtered = [t for t in filtered if t["category"] == sel_cat]
    if search.strip():
        q = search.lower()
        filtered = [
            t for t in filtered
            if q in t["title"].lower()
            or q in t["category"].lower()
            or q in t["description"].lower()
            or q in t["template"].lower()
        ]

    st.markdown(
        f'<div style="font-size:0.82rem;color:#4b5563;margin-bottom:20px;">'
        f'{len(filtered)} template{"s" if len(filtered) != 1 else ""} found</div>',
        unsafe_allow_html=True,
    )

    if not filtered:
        st.markdown(
            '<div style="text-align:center;color:#4b5563;padding:40px;">No templates match your search.</div>',
            unsafe_allow_html=True,
        )
        return

    # ── Template grid ─────────────────────────────────────────────────────────
    # Group by category if no active search
    if not search.strip() and sel_cat == "All":
        for cat in categories:
            cat_items = [t for t in filtered if t["category"] == cat]
            if not cat_items:
                continue
            fg, bg = cat_colors(cat)
            section_label(cat.upper())
            for item in cat_items:
                _render_template_card(item, fg, bg)
    else:
        for item in filtered:
            fg, bg = cat_colors(item["category"])
            _render_template_card(item, fg, bg)


def _render_template_card(item: dict, fg: str, bg: str):
    with st.expander(f"{item['title']}  ·  {item['category']}"):
        st.markdown(
            f"""
            <div style="padding:4px 0 12px;">
                <span style="display:inline-block;font-size:0.7rem;font-family:'Syne',sans-serif;
                             font-weight:700;letter-spacing:0.1em;text-transform:uppercase;
                             color:{fg};background:{bg};padding:3px 10px;border-radius:99px;
                             margin-bottom:10px;">{item['category']}</span>
                <div style="color:#94a3b8;font-size:0.9rem;margin-bottom:16px;line-height:1.55;">
                    {item['description']}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.code(item["template"], language=None)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔪  Evaluate this template", key=f"eval_{item['title']}"):
                st.session_state["selected_prompt"] = item["template"]
                st.info("Template loaded into Evaluate Prompt — navigate there to score it.")
        with col2:
            if st.button("🧪  Use in Practice Lab", key=f"prac_{item['title']}"):
                st.session_state["clipboard"] = item["template"]
                st.info("Template loaded into Practice Lab clipboard.")
