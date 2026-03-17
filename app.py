import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Prompt Engineering Lab",
    page_icon="🧠",
    layout="wide"
)

# ---------- NAVIGATION ----------
pages = {
    "Home": "home",
    "Learn Prompt Engineering": "learn",
    "Evaluate Prompt": "evaluate",
    "Practice Lab": "practice",
    "Prompt Templates": "templates",
    "Progress Dashboard": "progress"
}

selection = st.sidebar.radio("Navigation", list(pages.keys()))

# ---------- ROUTER ----------
if selection == "Home":
    st.title("🧠 Prompt Engineering Lab")
    st.subheader("Learn, practice, evaluate, and improve AI prompts")

    st.markdown("### Led by Dr. Loveleen Gaur")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("📚 Learn prompt engineering concepts")
    with col2:
        st.info("🧪 Practice with real-world tasks")
    with col3:
        st.info("📊 Evaluate using SHARP Framework")

    st.markdown("---")

    st.markdown("""
    ### What this platform does

    Prompt Engineering Lab helps you:
    - Design better prompts
    - Evaluate using SHARP
    - Learn through real examples
    - Practice across domains (marketing, HR, finance, etc.)

    The evaluation engine is powered by the **SHARP Framework**, developed by Dr. Loveleen Gaur.
    """)

elif selection == "Learn Prompt Engineering":
    import pages.learn as learn
    learn.show()

elif selection == "Evaluate Prompt":
    import pages.evaluate as evaluate
    evaluate.show()

elif selection == "Practice Lab":
    import pages.practice as practice
    practice.show()

elif selection == "Prompt Templates":
    import pages.templates as templates
    templates.show()

elif selection == "Progress Dashboard":
    import pages.progress as progress
    progress.show()
