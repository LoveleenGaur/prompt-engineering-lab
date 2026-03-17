import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Prompt Engineering Lab",
    page_icon="🧠",
    layout="wide"
)

# ---------- HIDE DEFAULT SIDEBAR ----------
st.markdown("""
<style>
section[data-testid="stSidebarNav"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# ---------- CUSTOM NAVIGATION ----------
st.sidebar.title("Navigation")

selection = st.sidebar.radio(
    "",
    [
        "Home",
        "Learn Prompt Engineering",
        "Evaluate Prompt",
        "Practice Lab",
        "Prompt Templates",
        "Progress Dashboard"
    ]
)

# ---------- HOME PAGE ----------
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

# ---------- ROUTING (IMPORTANT CHANGE HERE) ----------
elif selection == "Learn Prompt Engineering":
    import pages.learn

elif selection == "Evaluate Prompt":
    import pages.evaluate

elif selection == "Practice Lab":
    import pages.practice

elif selection == "Prompt Templates":
    import pages.templates

elif selection == "Progress Dashboard":
    import pages.progress
