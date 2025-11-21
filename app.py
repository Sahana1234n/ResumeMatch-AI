import streamlit as st
from src.resume_utils.resume_utils import get_report, extract_scores
from src.similarity import calculate_similarity_bert
from src.pdf_text_extraction.text_extraction import extract_text_from_pdf

# ------------------------------
# Session State initialization
# ------------------------------
if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if "job_text" not in st.session_state:
    st.session_state.job_text = ""

if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

# ------------------------------
# App Title
# ------------------------------
st.title("📝 ResumeMatch AI")
st.write("Upload your Resume & paste Job Description to get ATS + AI analysis.")

# ------------------------------
# Upload Section
# ------------------------------
resume_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
job_text = st.text_area("Job Description", placeholder="Paste the JD here...", height=200)

analyze_btn = st.button("Analyze Resume")

if analyze_btn:
    if resume_file is None or job_text.strip() == "":
        st.warning("⚠️ Please upload the resume and enter job description.")
    else:
        st.session_state.resume_text = extract_text_from_pdf(resume_file)
        st.session_state.job_text = job_text
        st.session_state.analyzed = True
        st.rerun()

# ------------------------------
# Analysis Section
# ------------------------------
if st.session_state.analyzed:

    col1, col2 = st.columns(2)

    with col1:
        st.info("Generating ATS Similarity Score...")
        ats_score = calculate_similarity_bert(
            st.session_state.resume_text,
            st.session_state.job_text
        )
        st.metric("ATS Similarity Score", f"{ats_score:.2f}")

    with col2:
        st.info("Generating AI Report...")
        report = get_report(
            st.session_state.resume_text,
            st.session_state.job_text
        )

        report_scores = extract_scores(report)
        avg_score = sum(report_scores) / len(report_scores) if report_scores else 0

        st.metric("AI Evaluation Score", f"{avg_score:.2f} / 5")

    st.divider()

    st.subheader("📊 AI Generated Resume Evaluation")

    st.markdown(
        f"""
         <div style='padding: 15px; 
                background-color: #f5f5f5; 
                border-radius: 10px; 
                line-height: 1.6;
                color: black;'>
            {report}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.download_button(
        label="⬇️ Download Report",
        data=report,
        file_name="resume_analysis_report.txt",
        mime="text/plain",
    )

    if st.button("🔄 Analyze Another Resume"):
        st.session_state.analyzed = False
        st.rerun()
