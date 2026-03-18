import streamlit as st
from utils.theme import inject_theme, page_header, section_label


def show():
    inject_theme()
    page_header("📈", "Progress Dashboard",
                "Track your practice sessions and evaluation scores for this session.")

    attempts = st.session_state.get("practice_attempts", [])
    evals    = st.session_state.get("eval_history", [])

    # ── Stats row ─────────────────────────────────────────────────────────────
    avg_score = round(sum(e["score"] for e in evals) / len(evals), 1) if evals else 0
    best_score = max((e["score"] for e in evals), default=0)

    c1, c2, c3, c4 = st.columns(4)
    stats = [
        (len(attempts), "Practice Attempts"),
        (len(evals),    "Evaluations Run"),
        (avg_score,     "Avg SHARP Score"),
        (best_score,    "Best Score"),
    ]
    for col, (val, label) in zip([c1, c2, c3, c4], stats):
        with col:
            color = "#e8b84b" if "Score" not in label else _score_color(val)
            st.markdown(
                f"""
                <div class="stat-card">
                    <div class="stat-value" style="color:{color};">{val}</div>
                    <div class="stat-label">{label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    if not attempts and not evals:
        st.markdown(
            """
            <div style="text-align:center;padding:60px 20px;">
                <div style="font-size:3rem;margin-bottom:16px;">📭</div>
                <div style="font-family:'Syne',sans-serif;font-weight:700;color:#f1f5f9;
                            font-size:1.1rem;margin-bottom:8px;">No activity yet</div>
                <div style="color:#4b5563;font-size:0.9rem;">
                    Head to Practice Lab to write prompts, or Evaluate Prompt to score one.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    col_left, col_right = st.columns([1, 1])

    # ── Evaluation history ────────────────────────────────────────────────────
    with col_left:
        section_label("EVALUATION HISTORY")
        if not evals:
            st.markdown('<div style="color:#4b5563;font-size:0.87rem;">No evaluations yet.</div>', unsafe_allow_html=True)
        else:
            for i, e in enumerate(reversed(evals), 1):
                color = _score_color(e["score"])
                emoji, label = _score_label(e["score"])
                pct = e["score"] / 10 * 100
                st.markdown(
                    f"""
                    <div class="sharp-card" style="margin-bottom:12px;padding:16px 20px;">
                        <div style="display:flex;justify-content:space-between;
                                    align-items:center;margin-bottom:10px;">
                            <div style="font-size:0.78rem;color:#4b5563;">#{i}</div>
                            <div style="font-family:'Syne',sans-serif;font-weight:800;
                                        font-size:1.3rem;color:{color};">{e['score']}/10</div>
                        </div>
                        <div style="background:rgba(255,255,255,0.06);border-radius:99px;
                                    height:5px;margin-bottom:10px;overflow:hidden;">
                            <div style="width:{pct}%;height:100%;background:{color};border-radius:99px;"></div>
                        </div>
                        <div style="font-size:0.72rem;font-family:'Syne',sans-serif;font-weight:700;
                                    letter-spacing:0.08em;color:{color};margin-bottom:6px;">
                            {emoji} {label}
                        </div>
                        <div style="font-size:0.83rem;color:#4b5563;font-style:italic;
                                    white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">
                            {e.get('prompt','')[:80]}…
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    # ── Practice attempts ─────────────────────────────────────────────────────
    with col_right:
        section_label(f"PRACTICE ATTEMPTS ({len(attempts)})")
        if not attempts:
            st.markdown('<div style="color:#4b5563;font-size:0.87rem;">No practice attempts yet.</div>', unsafe_allow_html=True)
        else:
            for i, a in enumerate(reversed(attempts), 1):
                with st.expander(f"#{i} — {a['task']}"):
                    st.markdown(
                        f"""
                        <div style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;
                                    color:#c8e6ff;line-height:1.65;background:#080f1a;
                                    border:1px solid rgba(255,255,255,0.06);border-radius:8px;
                                    padding:12px 14px;">
                            {a['prompt']}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    if st.button("🔪 Evaluate this prompt", key=f"prog_eval_{i}"):
                        st.session_state["selected_prompt"] = a["prompt"]
                        st.info("Prompt loaded into Evaluate Prompt — navigate there to score it.")

    # ── Clear session ─────────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div style="color:#4b5563;font-size:0.78rem;margin-bottom:8px;">Session data resets when you close the browser tab.</div>', unsafe_allow_html=True)
    if st.button("🗑  Clear all session data"):
        st.session_state.pop("practice_attempts", None)
        st.session_state.pop("eval_history", None)
        st.success("Session data cleared.")
        st.rerun()


def _score_color(score) -> str:
    if isinstance(score, float) or isinstance(score, int):
        s = float(score)
    else:
        return "#e8b84b"
    if s <= 3:   return "#f87171"
    if s <= 6:   return "#fbbf24"
    if s <= 8:   return "#4ade80"
    return "#2dd4bf"


def _score_label(score: int) -> tuple:
    if score <= 3:  return "🔴", "BLUNT"
    if score <= 6:  return "🟡", "GETTING THERE"
    if score <= 8:  return "🟢", "SHARP"
    return "⚡", "RAZOR SHARP"
