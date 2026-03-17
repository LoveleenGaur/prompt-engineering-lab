
import html
import re
import streamlit as st
from groq import Groq
from sharp_engine import SHARP_SYSTEM_PROMPT, build_evaluation_message

st.set_page_config(page_title="Evaluate Prompt", page_icon="📊", layout="wide")

api_key = st.secrets.get("GROQ_API_KEY", "")

def get_groq_client(key: str) -> Groq:
    return Groq(api_key=key)

def evaluate_with_groq(client: Groq, user_prompt: str, task_type: str) -> str:
    user_message = build_evaluation_message(user_prompt, task_type)
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.2,
        messages=[
            {"role": "system", "content": SHARP_SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
    )
    content = completion.choices[0].message.content
    if not content:
        raise ValueError("Groq returned an empty response.")
    return content

def safe_html(text: str) -> str:
    return html.escape(text).replace("\n", "<br>")

def extract_section(full_text: str, title: str) -> str:
    pattern = rf"###\s*{re.escape(title)}\s*(.*?)(?=\n###|\Z)"
    match = re.search(pattern, full_text, re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else ""

def extract_score_block(text: str):
    match = re.search(r"SHARP SCORE:\s*(\d+)\s*/\s*10\s*-\s*(.+)", text, re.IGNORECASE)
    if not match:
        return None, None
    return int(match.group(1)), match.group(2).strip()

def score_style(score: int):
    if score <= 3:
        return "🔴", "BLUNT", "#EF4444"
    if score <= 6:
        return "🟡", "GETTING THERE", "#F59E0B"
    if score <= 8:
        return "🟢", "SHARP", "#22C55E"
    return "⚡", "RAZOR SHARP", "#06B6D4"

def extract_dimension_explanation(section_text: str, dim_key: str):
    pattern = rf"\*\*{re.escape(dim_key)}:\s*\[?(\d)\]?\*\*\s*(.*?)(?=\n\*\*[SHARP]|\Z)"
    match = re.search(pattern, section_text, re.DOTALL)
    if not match:
        return None, ""
    return int(match.group(1)), match.group(2).strip()

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #081225 0%, #0b1730 100%);
    color: #f8fafc;
}
.result-shell {
    background: linear-gradient(180deg, rgba(17,28,54,0.95), rgba(13,23,48,0.98));
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 22px;
    padding: 24px;
    margin-top: 22px;
}
.score-card {
    background: linear-gradient(135deg, #101c36, #16284d);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 20px;
    padding: 24px;
    text-align: center;
    margin-bottom: 18px;
}
.score-number {
    font-size: 4rem;
    font-weight: 900;
    line-height: 1;
    margin: 0;
}
.dim-card {
    background: rgba(8,18,37,0.54);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 12px;
}
.improved-box {
    background: rgba(12,23,49,0.92);
    border: 1px solid rgba(34,197,94,0.55);
    border-radius: 16px;
    padding: 18px;
    color: #f8fafc;
    line-height: 1.75;
    font-size: 1rem;
    white-space: pre-wrap;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Evaluate Prompt")
st.caption("Prompt Engineering Lab · Powered by the SHARP Framework developed by Dr. Loveleen Gaur")

task_type = st.selectbox(
    "Prompt type",
    [
        "General",
        "Writing / Content",
        "Coding / Technical",
        "Marketing / Business",
        "Research / Academic",
        "Creative / Storytelling",
        "Data Analysis",
        "Email / Communication",
        "Education / Teaching",
        "Other"
    ]
)

user_prompt = st.text_area("Paste your prompt here", height=200)
evaluate_btn = st.button("Evaluate with SHARP")

if evaluate_btn:
    if not user_prompt.strip():
        st.warning("Please paste a prompt to evaluate.")
    elif not api_key:
        st.error("Groq API key was not found in Streamlit secrets.")
    else:
        client = get_groq_client(api_key)
        response_text = evaluate_with_groq(client, user_prompt, task_type)

        score_num, rating_text = extract_score_block(response_text)
        if score_num is None:
            st.error("The evaluator response did not include a valid SHARP score.")
        else:
            emoji, label, color = score_style(score_num)
            dim_section = extract_section(response_text, "DIMENSION BREAKDOWN")
            missing_section = extract_section(response_text, "WHAT'S MISSING")
            improved_section = extract_section(response_text, "IMPROVED SHARP PROMPT")
            tips_section = extract_section(response_text, "3 TIPS TO REMEMBER")

            st.markdown('<div class="result-shell">', unsafe_allow_html=True)
            st.markdown(
                f"""
                <div class="score-card">
                    <div class="score-number" style="color:{color};">{score_num}/10</div>
                    <div style="margin-top:12px; color:{color}; font-weight:800;">{emoji} {label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.subheader("📊 Dimension Breakdown")
            dims = ["S - Situation", "H - Hat", "A - Ask", "R - Rules", "P - Product"]
            for dim_key in dims:
                d_score, d_explain = extract_dimension_explanation(dim_section, dim_key)
                if d_score is not None:
                    st.markdown(
                        f"""
                        <div class="dim-card">
                            <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
                                <strong>{html.escape(dim_key)}</strong>
                                <span>{d_score}/2</span>
                            </div>
                            <div>{safe_html(d_explain)}</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

            if missing_section:
                st.subheader("🔎 What's Missing")
                st.markdown(safe_html(missing_section), unsafe_allow_html=True)

            if improved_section:
                st.subheader("✨ Improved SHARP Prompt")
                st.markdown(f'<div class="improved-box">{safe_html(improved_section)}</div>', unsafe_allow_html=True)
                st.code(improved_section, language=None)

            if tips_section:
                st.subheader("💡 3 Tips to Remember")
                st.markdown(safe_html(tips_section), unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)
