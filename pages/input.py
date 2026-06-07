import streamlit as st
import pdfplumber
import docx

from engine.analyzer import run_analysis


def _extract_text_from_file(uploaded_file) -> str:
    text = ""
    try:
        uploaded_file.seek(0)
        if uploaded_file.name.lower().endswith(".pdf"):
            # Coba pdfplumber dulu
            with pdfplumber.open(uploaded_file) as pdf:
                text = "\n".join(page.extract_text() or "" for page in pdf.pages)
            
            # Kalau gagal, fallback ke PyMuPDF
            if not text.strip():
                import fitz
                uploaded_file.seek(0)
                pdf_bytes = uploaded_file.read()
                doc = fitz.open(stream=pdf_bytes, filetype="pdf")
                text = "\n".join(page.get_text() for page in doc)

        elif uploaded_file.name.lower().endswith(".docx"):
            doc = docx.Document(uploaded_file)
            text = "\n".join(p.text for p in doc.paragraphs)

    except Exception as e:
        st.error(f"Gagal memproses file: {e}")
    return text


def render():
    st.markdown("""
    <div class="page-header">
        <div class="step-label">Step 1 of 2</div>
        <h2>Upload CV & Job Description</h2>
    </div>
    """, unsafe_allow_html=True)

    # ── CV input ──────────────────────────────────────────────────
    st.markdown('<span class="sec-label">📄 Resume / CV</span>', unsafe_allow_html=True)
    st.caption("Max 2MB · Format: PDF, DOCX")

    uploaded_resume = st.file_uploader(
        "Upload Resume", type=["pdf", "docx"],
        label_visibility="collapsed", key="resume_upload",
    )

    analyze_disabled = False
    if uploaded_resume and uploaded_resume.size > 2 * 1024 * 1024:
        st.error("❌ File melebihi 2MB.")
        analyze_disabled = True

    st.markdown("**atau** paste teks CV:")
    resume_paste = st.text_area(
        "Resume text", placeholder="Paste isi CV kamu di sini...",
        height=150, label_visibility="collapsed",
    )

    st.markdown("---")

    # ── Job Description input ─────────────────────────────────────
    st.markdown('<span class="sec-label">💼 Job Description</span>', unsafe_allow_html=True)
    st.caption("Paste requirements dari lowongan yang dituju")

    job_paste = st.text_area(
        "Job Description", placeholder="Paste job description di sini...",
        height=200, label_visibility="collapsed",
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Kembali", use_container_width=True):
            st.session_state.page = "welcome"
            st.rerun()
    with col2:
        analyze = st.button("Analisis Sekarang →", use_container_width=True, disabled=analyze_disabled)

    if analyze:
        resume_text = _extract_text_from_file(uploaded_resume) if uploaded_resume else ""
        st.write(f"DEBUG: panjang teks = {len(resume_text)} karakter")
        if not resume_text and resume_paste:
            resume_text = resume_paste.strip()
        job_text = job_paste.strip()

        if not resume_text:
            st.warning("⚠️ CV belum diisi. Upload file atau paste teks.")
        elif not job_text:
            st.warning("⚠️ Job description wajib diisi.")
        else:
            with st.spinner("Menganalisis CV..."):
                try:
                    result = run_analysis(resume_text, job_text)
                    st.session_state.analysis_result = result
                    st.session_state.resume_text_raw = resume_text
                    st.session_state.job_text_raw    = job_text
                    st.session_state.page            = "result"
                    st.rerun()
                except Exception as e:
                    st.error(f"Analisis gagal: {e}")
