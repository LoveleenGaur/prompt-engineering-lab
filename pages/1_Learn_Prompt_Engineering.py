
import streamlit as st

st.set_page_config(page_title="Learn Prompt Engineering", page_icon="📚", layout="wide")

st.title("📚 Learn Prompt Engineering")
st.caption("Prompt Engineering Lab · Led by Dr. Loveleen Gaur")

st.markdown("""
### What is prompt engineering?
Prompt engineering is the practice of designing instructions that help AI systems produce more accurate,
useful, and structured outputs.

A strong prompt usually includes:
- context
- role
- clear task
- constraints
- expected output

### Why it matters
Weak prompts produce vague output. Strong prompts improve accuracy, relevance, consistency, and usability.

### Frameworks in this platform
This platform teaches prompt engineering broadly, while evaluation is powered by the **SHARP Framework**,
developed by Dr. Loveleen Gaur.
""")

with st.expander("Module 1 · Foundations", expanded=True):
    st.write(
        "Learn the difference between vague prompts and structured prompts. Focus on clarity, context, and output control."
    )

with st.expander("Module 2 · The SHARP Framework"):
    st.write("""
**S — Situation**: background and context  
**H — Hat**: role or persona for the AI  
**A — Ask**: the exact task  
**R — Rules**: constraints and boundaries  
**P — Product**: output format
""")

with st.expander("Module 3 · Weak vs Strong Prompt"):
    st.write("""
**Weak:** Write about leadership.

**Stronger:**  
You are a management professor. Write a 300-word explanation of transformational leadership for MBA students.
Use simple language, include one real-world example, and end with three key takeaways in bullet points.
""")

st.success("Next step: open **Evaluate Prompt** in the sidebar.")
