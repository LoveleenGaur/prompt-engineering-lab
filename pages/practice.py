import json
import streamlit as st
from utils.theme import inject_theme, page_header, section_label

DIFFICULTY_PILL = {
    "Beginner":     "pill pill-green",
    "Intermediate": "pill pill-gold",
    "Advanced":     "pill pill-red",
}
DOMAIN_PILL = "pill pill-blue"


def show():
    inject_theme()
    page_header("🧪", "Practice Lab",
                "Write SHARP-structured prompts for real-world business scenarios.")

    with open("data/practice_tasks.json", "r", encoding="utf-8") as f:
        tasks = json.load(f)

    # ── Filter bar ────────────────────────────────────────────────────────────
    all_domains = sorted(set(t.get("domain", "General") for t in tasks))
    all_difficulties = ["All", "Beginner", "Intermediate", "Advanced"]

    col1, col2, col3 = st.columns([3, 2, 2])
    with col1:
        search_q = st.text_input("Search tasks", placeholder="Filter by title or domain…")
    with col2:
        sel_domain = st.selectbox("Domain", ["All"] + all_domains)
    with col3:
        sel_diff = st.selectbox("Difficulty", all_difficulties)

    filtered = tasks
    if sel_domain != "All":
        filtered = [t for t in filtered if t.get("domain") == sel_domain]
    if sel_diff != "All":
        filtered = [t for t in filtered if t.get("difficulty") == sel_diff]
    if search_q.strip():
        q = search_q.lower()
        filtered = [t for t in filtered if q in t["title"].lower() or q in t.get("domain","").lower()]

    task_titles = [t["title"] for t in filtered]
    if not task_titles:
        st.markdown(
            '<div style="color:#4b5563;padding:20px;text-align:center;">No tasks match your filters.</div>',
            unsafe_allow_html=True,
        )
        return

    selected_title = st.selectbox("Select a practice task", task_titles)
    task = next(t for t in filtered if t["title"] == selected_title)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Task card ─────────────────────────────────────────────────────────────
    diff_class = DIFFICULTY_PILL.get(task.get("difficulty", "Beginner"), "pill pill-blue")
    st.markdown(
        f"""
        <div class="sharp-card">
            <div style="display:flex;gap:8px;margin-bottom:14px;">
                <span class="{diff_class}">{task.get('difficulty','')}</span>
                <span class="{DOMAIN_PILL}">{task.get('domain','')}</span>
            </div>
            <div style="font-family:'Syne',sans-serif;font-weight:700;font-size:1.15rem;
                        color:#f1f5f9;margin-bottom:10px;">{task['title']}</div>
            <div style="color:#94a3b8;font-size:0.95rem;line-height:1.7;">{task['task']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Hint ──────────────────────────────────────────────────────────────────
    if task.get("hint"):
        st.markdown(
            f"""
            <div style="background:rgba(232,184,75,0.05);border:1px solid rgba(232,184,75,0.15);
                        border-radius:10px;padding:12px 18px;margin-bottom:16px;">
                <span style="color:#e8b84b;font-size:0.85rem;">💡 <strong>Hint:</strong> {task['hint']}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ── Success criteria ──────────────────────────────────────────────────────
    section_label("SUCCESS CRITERIA")
    criteria_html = "".join(
        f"""<div style="display:flex;gap:10px;align-items:flex-start;
                        padding:8px 0;border-bottom:1px solid rgba(255,255,255,0.04);">
                <span style="color:#4ade80;margin-top:1px;">✓</span>
                <span style="color:#94a3b8;font-size:0.9rem;">{c}</span>
            </div>"""
        for c in task.get("success_criteria", [])
    )
    st.markdown(
        f'<div style="margin-bottom:20px;">{criteria_html}</div>',
        unsafe_allow_html=True,
    )

    # ── SHARP reminder ────────────────────────────────────────────────────────
    st.markdown(
        """
        <div style="background:rgba(45,212,191,0.05);border:1px solid rgba(45,212,191,0.15);
                    border-radius:10px;padding:12px 18px;margin-bottom:20px;">
            <span style="color:#2dd4bf;font-size:0.85rem;">
                📝 <strong>Remember SHARP:</strong>
                [S] Situation · [H] Hat · [A] Ask · [R] Rules · [P] Product
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Prompt editor ─────────────────────────────────────────────────────────
    # Pre-fill from clipboard if available
    clipboard = st.session_state.pop("clipboard", None)
    draft_key = f"draft_{selected_title}"
    if clipboard and not st.session_state.get(draft_key):
        st.session_state[draft_key] = clipboard

    student_prompt = st.text_area(
        "Write your SHARP prompt here",
        height=200,
        key=draft_key,
        placeholder=(
            "[S] Context: ...\n"
            "[H] You are a ...\n"
            "[A] Task: ...\n"
            "[R] Constraints: ...\n"
            "[P] Output format: ..."
        ),
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾  Save attempt", use_container_width=True):
            if student_prompt.strip():
                attempts = st.session_state.get("practice_attempts", [])
                attempts.append({"task": selected_title, "prompt": student_prompt})
                st.session_state["practice_attempts"] = attempts
                st.success("Attempt saved! Head to **Evaluate Prompt** to score it.")
            else:
                st.warning("Write a prompt before saving.")
    with col2:
        if st.button("🔪  Save & Evaluate", use_container_width=True):
            if student_prompt.strip():
                attempts = st.session_state.get("practice_attempts", [])
                attempts.append({"task": selected_title, "prompt": student_prompt})
                st.session_state["practice_attempts"] = attempts
                st.session_state["selected_prompt"] = student_prompt
                st.info("Prompt saved and loaded into Evaluate Prompt — navigate there to score it.")
            else:
                st.warning("Write a prompt before evaluating.")

    # ── Previous attempts ─────────────────────────────────────────────────────
    attempts = st.session_state.get("practice_attempts", [])
    task_attempts = [a for a in attempts if a["task"] == selected_title]

    if task_attempts:
        st.markdown("<br>", unsafe_allow_html=True)
        section_label(f"PREVIOUS ATTEMPTS FOR THIS TASK ({len(task_attempts)})")
        for i, a in enumerate(reversed(task_attempts), 1):
            with st.expander(f"Attempt {i}"):
                st.markdown(
                    f"""
                    <div style="font-family:'JetBrains Mono',monospace;font-size:0.87rem;
                                color:#c8e6ff;line-height:1.7;background:#080f1a;
                                border:1px solid rgba(255,255,255,0.06);border-radius:8px;
                                padding:14px 16px;">
                        {a['prompt']}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                if st.button("Load into editor", key=f"load_{selected_title}_{i}"):
                    st.session_state[draft_key] = a["prompt"]
                    st.rerun()
