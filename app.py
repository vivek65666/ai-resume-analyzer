import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from components.sidebar import render_sidebar
from components.ui import render_dashboard_metrics
from utils.parser import extract_text_from_pdf
from utils.helper import analyze_resume_with_llm

st.set_page_config(page_title="Enterprise AI Resume Analyzer", page_icon="💼", layout="wide")
config = render_sidebar()

PRESET_MANDATES = {
    "Senior AI Engineer": "Looking for a Senior AI Engineer with deep expertise in Python, Large Language Models, Prompt Isolation, Streamlit, Vector Databases, and production Docker container configurations.",
    "Data Scientist": "Seeking a Data Scientist proficient in Python, SQL, pandas, Scikit-Learn, training predictive machine learning loops, and engineering analytical dashboards.",
    "Full-Stack Developer": "Requirements include Node.js, React, TypeScript, PostgreSQL, RESTful API routing pipelines, and automated CI/CD deployments via GitHub Actions."
}

st.title("💼 Automated Preliminary Pipeline Ingestion")
st.subheader("ATS Compliance Parser & Context Evaluation Matrix")

col_input, col_display = st.columns([1, 1])

with col_input:
    st.markdown("### 📋 Input Validation Targets")
    default_jd = ""
    if config["preset"] in PRESET_MANDATES:
        default_jd = PRESET_MANDATES[config["preset"]]
        
    job_desc_input = st.text_area("Target Corporate Job Mandate", value=default_jd, height=200)
    uploaded_file = st.file_uploader("Upload Candidate Resume (PDF layout constraints)", type=["pdf"])
    run_analysis = st.button("🚀 Execute Structural Extraction Analysis", type="primary", use_container_width=True)

with col_display:
    if run_analysis:
        if not job_desc_input:
            st.error("Operation Aborted: Target corporate mandate cannot be blank.")
        elif not uploaded_file:
            st.error("Operation Aborted: Missing valid candidate target document payload.")
        else:
            with st.spinner("Executing runtime vector extraction, tokenizing byte arrays..."):
                try:
                    raw_resume_text = extract_text_from_pdf(uploaded_file)
                    analysis_payload = analyze_resume_with_llm(
                        resume_text=raw_resume_text,
                        job_description=job_desc_input,
                        model=config["model"]
                    )
                    render_dashboard_metrics(analysis_payload)
                except Exception as error:
                    st.error(f"Fatal operational pipeline exception error: {error}")
    else:
        st.info("System Ready. Upload a validation asset framework to begin real-time compilation loops.")