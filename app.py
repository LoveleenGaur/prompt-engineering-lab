
"""
SHARP Prompt Evaluator
Clean responsive UI version
Built on the SHARP Framework by Loveleen Gaur
Powered by Groq
"""

import re
import streamlit as st
from groq import Groq
from sharp_engine import SHARP_SYSTEM_PROMPT, build_evaluation_message

st.set_page_config(
    page_title="SHARP Prompt Evaluator",
    page_icon="🔪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

api_key = st.secrets.get("GROQ_API_KEY", "")

def get_groq_client(api_key: str) -> Groq:
    return Groq(api_key=api_key)

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
    return completion.choices[0].message.content

st.markdown("""
<style>
.stApp { background:#0B1020; color:#F8FAFC; }

[data-testid="stSidebar"] { display:none; }

.hero {
background:linear-gradient(135deg,#0F172A,#1E293B);
border-radius:18px;
padding:40px;
text-align:center;
margin-bottom:30px;
border:1px solid #1F2A44;
}

.hero h1 {font-size:40px;margin-bottom:10px;}
.hero p {color:#94A3B8;}

.sharp-grid{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:20px;}

.sharp-box{
background:#111827;
border:1px solid #24324A;
padding:12px 20px;
border-radius:10px;
text-align:center;
min-width:90px;
}

.sharp-letter{color:#FF7A1A;font-weight:700;font-size:20px;}

textarea{background:#111827 !important;}

.stButton button{
background:#FF7A1A;
border:none;
color:white;
padding:14px 26px;
border-radius:10px;
font-weight:600;
}

.stButton button:hover{background:#FF933D;}

.result-card{
background:#121A2B;
border:1px solid #24324A;
padding:25px;
border-radius:16px;
margin-top:30px;
}

.score{font-size:48px;font-weight:700;text-align:center;}

.dimension{
background:#0F172A;
padding:15px;
border-radius:10px;
margin-top:10px;
border:1px solid #24324A;
}

.prompt-box{
background:#0F172A;
border:1px solid #22C55E;
padding:20px;
border-radius:12px;
margin-top:20px;
}

@media (max-width:768px){
.hero h1{font-size:28px;}
.score{font-size:34px;}
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>🔪 SHARP Prompt Evaluator</h1>
<p>Evaluate and improve your AI prompts using the SHARP framework</p>

<div class="sharp-grid">
<div class="sharp-box"><div class="sharp-letter">S</div>Situation</div>
<div class="sharp-box"><div class="sharp-letter">H</div>Hat</div>
<div class="sharp-box"><div class="sharp-letter">A</div>Ask</div>
<div class="sharp-box"><div class="sharp-letter">R</div>Rules</div>
<div class="sharp-box"><div class="sharp-letter">P</div>Product</div>
</div>
</div>
""", unsafe_allow_html=True)

st.subheader("Evaluate your prompt")

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
])

user_prompt = st.text_area(
"Paste your prompt",
height=180,
placeholder="Example: Explain AI to a beginner"
)

evaluate_btn = st.button("Evaluate My Prompt")

if evaluate_btn:

    if not user_prompt.strip():
        st.warning("Please enter a prompt")
    elif not api_key:
        st.error("Groq API key missing in secrets")
    else:

        client = get_groq_client(api_key)
        response = evaluate_with_groq(client,user_prompt,task_type)

        st.markdown('<div class="result-card">', unsafe_allow_html=True)

        score_match = re.search(r'SHARP SCORE:\s*(\d+)/10\s*-\s*(.+)', response)

        if score_match:
            score = score_match.group(1)
            rating = score_match.group(2)
            st.markdown(f'<div class="score">{score}/10</div>', unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:center'>{rating}</p>", unsafe_allow_html=True)

        sections = response.split("###")

        for section in sections:
            section = section.strip()

            if "WHAT'S MISSING" in section:
                st.subheader("What's Missing")
                st.write(section.replace("WHAT'S MISSING",""))

            elif "IMPROVED SHARP PROMPT" in section:
                st.subheader("Improved Prompt")
                content = section.replace("IMPROVED SHARP PROMPT","")
                st.markdown(f"<div class='prompt-box'>{content}</div>",unsafe_allow_html=True)

            elif "3 TIPS TO REMEMBER" in section:
                st.subheader("Tips")
                st.write(section.replace("3 TIPS TO REMEMBER",""))

        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Built on the SHARP Framework by Loveleen Gaur")
