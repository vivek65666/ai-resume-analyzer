import streamlit as st

def render_dashboard_metrics(analysis_result: dict):
    st.markdown("## 📊 Optimization Analytics Dashboard")
    st.divider()
    
    score = analysis_result.get("ats_score", 0)
    verdict = analysis_result.get("verdict", "Unknown")
    
    col1, col2 = st.columns(2)
    with col1:
        if score >= 80:
            st.success(f"### ATS Compatibility: {score}%")
        elif score >= 50:
            st.warning(f"### ATS Compatibility: {score}%")
        else:
            st.error(f"### ATS Compatibility: {score}%")
            
    with col2:
        st.info(f"### Recruitment Verdict:\n{verdict}")
        
    st.divider()
    col_match, col_miss = st.columns(2)
    
    with col_match:
        st.markdown("#### ✅ Detected Technical Matches")
        matched_skills = analysis_result.get("skills_match", [])
        if matched_skills:
            for skill in matched_skills:
                st.markdown(f"`{skill}`")
        else:
            st.caption("No matching structural keywords isolated.")
            
    with col_miss:
        st.markdown("#### ❌ Critical Skills Gaps")
        missing_skills = analysis_result.get("missing_skills", [])
        if missing_skills:
            for skill in missing_skills:
                st.markdown(f"<span style='color:#ef5350; font-weight:bold;'>• {skill}</span>", unsafe_allow_html=True)
        else:
            st.caption("No explicit skills omissions flagged.")
            
    st.divider()
    st.markdown("### 📝 Granular Bullet Point Improvements")
    improvements = analysis_result.get("structural_improvements", [])
    if improvements:
        for point in improvements:
            st.info(point)
    else:
        st.success("Resume structure fully conforms with baseline expectations.")