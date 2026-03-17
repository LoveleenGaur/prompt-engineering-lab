import streamlit as st

def show():
    st.title("📚 Learn Prompt Engineering")
    st.caption("A structured guide to designing high-quality AI prompts.")

    st.markdown("---")

    # --------------------------------------------------
    # SECTION 1: WHAT IS PROMPT ENGINEERING
    # --------------------------------------------------
    st.header("🔹 What is Prompt Engineering?")

    st.markdown("""
    Prompt engineering is the process of designing inputs that guide AI systems to produce accurate, structured, and useful outputs.

    A good prompt reduces ambiguity and increases control over:
    - quality of response
    - structure of output
    - relevance of content
    """)

    # --------------------------------------------------
    # SECTION 2: WHY PROMPTS FAIL
    # --------------------------------------------------
    st.header("❌ Why Prompts Fail")

    st.markdown("""
    Most prompts fail because they are:
    - Too vague → "Write about marketing"
    - Missing role → AI doesn't know perspective
    - No structure → output becomes messy
    - No constraints → output becomes too long or irrelevant
    """)

    st.markdown("---")

    # --------------------------------------------------
    # SECTION 3: SHARP FRAMEWORK
    # --------------------------------------------------
    st.header("🧠 The SHARP Framework")

    st.markdown("""
    SHARP helps you structure prompts clearly:

    - **S — Situation** → Context  
    - **H — Hat** → Role  
    - **A — Ask** → Task  
    - **R — Rules** → Constraints  
    - **P — Product** → Output format  
    """)

    st.success("If a prompt is missing 2–3 of these → quality drops significantly.")

    # --------------------------------------------------
    # SECTION 4: WEAK VS STRONG PROMPTS
    # --------------------------------------------------
    st.header("⚖️ Weak vs Strong Prompts")

    examples = [
        (
            "Marketing",
            "Write about marketing",
            "You are a marketing strategist. Explain digital marketing strategies for startups. Include 3 examples and present in bullet points."
        ),
        (
            "HR",
            "Write HR policy",
            "You are an HR manager. Create a remote work policy including eligibility, expectations, and compliance rules. Present with headings."
        ),
        (
            "Finance",
            "Explain budgeting",
            "You are a finance expert. Explain zero-based budgeting with advantages, disadvantages, and a real-world example."
        )
    ]

    for domain, weak, strong in examples:
        with st.expander(f"{domain} Example"):
            st.markdown(f"❌ **Weak Prompt:** {weak}")
            st.markdown(f"✅ **Strong Prompt:** {strong}")

    st.markdown("---")

    # --------------------------------------------------
    # SECTION 5: MANAGEMENT DOMAIN EXAMPLES
    # --------------------------------------------------
    st.header("📊 Management Domain Examples")

    domain_examples = [
        "Marketing strategy for product launch",
        "HR policy for remote teams",
        "Financial analysis for budgeting",
        "Business strategy for market expansion",
        "Operations improvement plan",
        "Leadership coaching advice",
        "Customer experience improvement",
        "Project management roadmap",
        "Startup idea evaluation",
        "Risk management analysis"
    ]

    for ex in domain_examples:
        st.write(f"- {ex}")

    st.markdown("---")

    # --------------------------------------------------
    # SECTION 6: COMMON MISTAKES
    # --------------------------------------------------
    st.header("⚠️ Common Prompt Mistakes")

    st.markdown("""
    Avoid these:

    - No role → "Explain AI"
    - No structure → long paragraphs with no clarity
    - No constraints → too generic output
    - No output format → hard to use results
    """)

    st.markdown("---")

    # --------------------------------------------------
    # SECTION 7: REWRITE PRACTICE
    # --------------------------------------------------
    st.header("🧪 Practice: Improve This Prompt")

    weak_prompt = st.text_area(
        "Rewrite this weak prompt using SHARP:",
        value="Explain marketing",
        height=100
    )

    if st.button("Show Example Improvement"):
        st.success("""
        You are a marketing strategist. Explain digital marketing strategies for startups.
        Include 3 examples and present the output in bullet points.
        """)

    st.markdown("---")

    # --------------------------------------------------
    # SECTION 8: NEXT STEP
    # --------------------------------------------------
    st.success("Next → Go to Practice Lab and start writing prompts.")
