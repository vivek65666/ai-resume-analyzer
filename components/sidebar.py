import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.title("⚙️ System Config")
        st.markdown("Configure underlying pipeline behavior parameters.")
        
        # Ensure Gemini models are the active choices
        model_choice = st.selectbox(
            "LLM Engine Core",
            options=["gemini-2.5-flash", "gemini-2.5-pro"],
            index=0
        )
        st.divider()
        st.markdown("### Pre-set Job Profiles")
        preset_role = st.selectbox(
            "Quick Load Job Mandate Template",
            options=["Custom Input", "Senior AI Engineer", "Data Scientist", "Full-Stack Developer"]
        )
        st.divider()
        st.caption("AI Resume Analyzer v1.0.0 | Engine Operational")
        return {"model": model_choice, "preset": preset_role}