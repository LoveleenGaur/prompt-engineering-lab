import streamlit as st

# ── Page config (MUST be first Streamlit call) ──────────────────────────────
st.set_page_config(
    page_title="Prompt Engineering Lab",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

from utils.theme import inject_theme

inject_theme()

# ── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        """
        <div style="padding: 20px 8px 24px; border-bottom: 1px solid rgba(255,255,255,0.07); margin-bottom: 16px;">
            <div style="font-family:'Syne',sans-serif; font-size:1.35rem; font-weight:800;
                        color:#f1f5f9; letter-spacing:-0.02em; line-height:1.2;">
                Prompt<br>Engineering<br>
                <span style="color:#e8b84b;">Lab</span>
            </div>
            <div style="font-size:0.72rem; color:#4b5563; margin-top:8px;
                        text-transform:uppercase; letter-spacing:0.1em;">
                Powered by SHARP Framework
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    selection = st.radio(
        "",
        [
            "🏠  Home",
            "📚  Learn",
            "🔪  Evaluate Prompt",
            "🧪  Practice Lab",
            "📁  Templates",
            "📈  Progress",
        ],
        label_visibility="collapsed",
    )

    st.markdown(
        """
        <div style="padding: 24px 8px 0; margin-top: 32px; border-top: 1px solid rgba(255,255,255,0.07);">
            <div style="font-size:0.72rem; color:#4b5563; text-align:center; line-height:1.7;">
                SHARP Framework<br>
                <span style="color:#6b7280;">by Dr. Loveleen Gaur</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ── Routing ──────────────────────────────────────────────────────────────────
page = selection.split("  ", 1)[-1].strip()

if page == "Home":
    st.markdown(
        """
        <div style="padding: 48px 0 32px; text-align:center;">
            <div style="font-family:'Syne',sans-serif; font-size:0.72rem; font-weight:700;
                        letter-spacing:0.18em; text-transform:uppercase; color:#e8b84b; margin-bottom:16px;">
                PROMPT ENGINEERING LAB
            </div>
            <h1 style="font-family:'Syne',sans-serif; font-size:clamp(2.2rem,5vw,3.8rem);
                       font-weight:800; letter-spacing:-0.03em; color:#f1f5f9;
                       line-height:1.1; margin:0 0 16px;">
                Write prompts that<br>
                <span style="color:#e8b84b;">actually work.</span>
            </h1>
            <p style="color:#94a3b8; font-size:1.05rem; max-width:520px; margin:0 auto 40px;
                      line-height:1.65;">
                Learn, practice, and evaluate AI prompts using the
                <strong style="color:#f1f5f9;">SHARP Framework</strong> —
                developed by Dr. Loveleen Gaur.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="sharp-letters">
            <span title="Situation">S</span>
            <span title="Hat / Role">H</span>
            <span title="Ask / Task">A</span>
            <span title="Rules / Constraints">R</span>
            <span title="Product / Output">P</span>
        </div>
        <div style="text-align:center; margin-bottom:48px;">
            <span style="font-size:0.8rem; color:#4b5563; letter-spacing:0.04em;">
                Situation · Hat · Ask · Rules · Product
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4, c5 = st.columns(5)
    cards = [
        ("📚", "Learn", "Structured lessons on prompt design and the SHARP method."),
        ("🔪", "Evaluate", "Score any prompt 0–10 across all 5 SHARP dimensions."),
        ("🧪", "Practice", "Real-world scenarios across business domains."),
        ("📁", "Templates", "25+ ready-to-use SHARP-formatted prompt templates."),
        ("📈", "Progress", "Track your practice sessions and improvement over time."),
    ]
    for col, (icon, title, desc) in zip([c1, c2, c3, c4, c5], cards):
        with col:
            st.markdown(
                f"""
                <div class="feature-card">
                    <div class="feature-icon">{icon}</div>
                    <div class="feature-title">{title}</div>
                    <div class="feature-desc">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="background:linear-gradient(135deg,#0c1220 0%,#101828 100%);
                    border:1px solid rgba(255,255,255,0.07); border-radius:20px;
                    padding:32px 36px; max-width:720px; margin:0 auto;">
            <div style="font-family:'Syne',sans-serif; font-size:0.72rem; font-weight:700;
                        letter-spacing:0.14em; text-transform:uppercase; color:#e8b84b;
                        margin-bottom:16px;">
                THE SHARP FRAMEWORK — AT A GLANCE
            </div>
            <div style="display:flex; flex-direction:column; gap:10px;">
                <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.06); border-radius:10px; padding:12px 16px; display:flex; gap:14px; align-items:center;">
                    <span style="font-family:'Syne',sans-serif; font-weight:800; color:#e8b84b; font-size:1.1rem; min-width:20px;">S</span>
                    <span style="color:#94a3b8; font-size:0.9rem;"><strong style="color:#f1f5f9;">Situation</strong> — Context &amp; background for the task</span>
                </div>
                <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.06); border-radius:10px; padding:12px 16px; display:flex; gap:14px; align-items:center;">
                    <span style="font-family:'Syne',sans-serif; font-weight:800; color:#e8b84b; font-size:1.1rem; min-width:20px;">H</span>
                    <span style="color:#94a3b8; font-size:0.9rem;"><strong style="color:#f1f5f9;">Hat</strong> — Role or expert persona for the AI to adopt</span>
                </div>
                <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.06); border-radius:10px; padding:12px 16px; display:flex; gap:14px; align-items:center;">
                    <span style="font-family:'Syne',sans-serif; font-weight:800; color:#e8b84b; font-size:1.1rem; min-width:20px;">A</span>
                    <span style="color:#94a3b8; font-size:0.9rem;"><strong style="color:#f1f5f9;">Ask</strong> — The clear, specific task or action required</span>
                </div>
                <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.06); border-radius:10px; padding:12px 16px; display:flex; gap:14px; align-items:center;">
                    <span style="font-family:'Syne',sans-serif; font-weight:800; color:#e8b84b; font-size:1.1rem; min-width:20px;">R</span>
                    <span style="color:#94a3b8; font-size:0.9rem;"><strong style="color:#f1f5f9;">Rules</strong> — Constraints, boundaries, and tone guidelines</span>
                </div>
                <div style="background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.06); border-radius:10px; padding:12px 16px; display:flex; gap:14px; align-items:center;">
                    <span style="font-family:'Syne',sans-serif; font-weight:800; color:#e8b84b; font-size:1.1rem; min-width:20px;">P</span>
                    <span style="color:#94a3b8; font-size:0.9rem;"><strong style="color:#f1f5f9;">Product</strong> — Expected output format and structure</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif page == "Learn":
    from pages import learn
    learn.show()

elif page == "Evaluate Prompt":
    from pages import evaluate
    evaluate.show()

elif page == "Practice Lab":
    from pages import practice
    practice.show()

elif page == "Templates":
    from pages import templates
    templates.show()

elif page == "Progress":
    from pages import progress
    progress.show()
