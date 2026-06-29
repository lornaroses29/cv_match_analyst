import streamlit as st
import pdfplumber
import docx
from pathlib import Path

from engine.analyzer import run_analysis
from engine.cv_validator import validate_cv_template


def _extract_text_from_file(uploaded_file) -> str:
    text = ""

    try:
        if uploaded_file.name.lower().endswith(".pdf"):
            with pdfplumber.open(uploaded_file) as pdf:
                text = "\n".join(
                    page.extract_text() or ""
                    for page in pdf.pages
                )

        elif uploaded_file.name.lower().endswith(".docx"):
            doc = docx.Document(uploaded_file)
            text = "\n".join(
                p.text
                for p in doc.paragraphs
            )

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

    #################################################
    # TEMPLATE CV
    #################################################

    with st.expander(
        "📄 Lihat Template CV ATS yang Didukung"
    ):
        st.markdown("""
        ### Struktur CV yang Direkomendasikan

        ✅ Profil Singkat  
        ✅ Pendidikan  
        ✅ Pengalaman Kerja  
        ✅ Proyek / Organisasi  
        ✅ Skill / Keahlian  
        ✅ Sertifikat (Opsional)  
        ✅ Kontak

        ---
        ### Contoh Struktur

        Nama Lengkap  
        Email | Nomor HP | LinkedIn

        #### Profil
        Mahasiswa Data Science dengan minat di bidang AI.

        #### Pendidikan
        - Universitas ABC
        - IPK 3.80

        #### Pengalaman
        - Mengembangkan aplikasi web.
        - Meningkatkan performa sistem sebesar 30%.

        #### Proyek
        - Sistem rekomendasi film.

        #### Skill
        Python, SQL, Machine Learning
        """)

    #################################################
    # DOWNLOAD TEMPLATE
    #################################################

    template_path = Path(
        "templates/cv_template.docx"
    )

    if template_path.exists():
        with open(template_path, "rb") as file:
            st.download_button(
                "⬇️ Download Template CV ATS",
                data=file,
                file_name="Template_CV_ATS.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

    st.markdown("---")

    #################################################
    # CV INPUT
    #################################################

    st.markdown(
        '<span class="sec-label">📄 Resume / CV</span>',
        unsafe_allow_html=True,
    )

    st.caption(
        "Max 2MB · Format: PDF atau DOCX"
    )

    uploaded_resume = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"],
        label_visibility="collapsed",
        key="resume_upload",
    )

    analyze_disabled = False

    if (
        uploaded_resume
        and uploaded_resume.size > 2 * 1024 * 1024
    ):
        st.error(
            "❌ File melebihi ukuran 2MB."
        )
        analyze_disabled = True

    st.info("""
    Format yang didukung:

    • Bahasa Indonesia  
    • PDF atau DOCX  
    • Memiliki bagian Pendidikan, Pengalaman, dan Skill  
    • Tidak berupa scan gambar.
    """)

    st.markdown("**atau paste isi CV:**")

    resume_paste = st.text_area(
        "Resume Text",
        placeholder="Paste isi CV kamu di sini...",
        height=150,
        label_visibility="collapsed",
    )

    #################################################
    # PREVIEW VALIDASI TEMPLATE
    #################################################

    preview_resume = ""

    if uploaded_resume:
        preview_resume = _extract_text_from_file(
            uploaded_resume
        )
    elif resume_paste:
        preview_resume = resume_paste

    if preview_resume:

        template_result = (
            validate_cv_template(
                preview_resume
            )
        )

        st.markdown("### Template Score")

        st.progress(
            template_result["score"]
        )

        st.metric(
            "Kelengkapan Template",
            f"{round(template_result['score']*100)}%"
        )

        if template_result["is_valid"]:
            st.success(
                "✅ Template CV didukung."
            )
        else:
            st.warning(
                "⚠️ Template CV belum sesuai."
            )

            if template_result["missing"]:
                st.write(
                    "Bagian yang belum ditemukan:"
                )

                for item in template_result["missing"]:
                    st.write(
                        f"• {item.capitalize()}"
                    )

    st.markdown("---")

    #################################################
    # JOB DESCRIPTION
    #################################################

    st.markdown(
        '<span class="sec-label">💼 Job Description</span>',
        unsafe_allow_html=True,
    )

    st.caption(
        "Paste requirements dari lowongan"
    )

    job_paste = st.text_area(
        "Job Description",
        placeholder="Paste job description di sini...",
        height=200,
        label_visibility="collapsed",
    )

    st.markdown("<br>", unsafe_allow_html=True)

    #################################################
    # BUTTON
    #################################################

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "← Kembali",
            use_container_width=True
        ):
            st.session_state.page = "welcome"
            st.rerun()

    with col2:
        analyze = st.button(
            "Analisis Sekarang →",
            use_container_width=True,
            disabled=analyze_disabled,
        )

    #################################################
    # ANALISIS
    #################################################

    if analyze:

        resume_text = ""

        if uploaded_resume:
            resume_text = (
                _extract_text_from_file(
                    uploaded_resume
                )
            )

        elif resume_paste:
            resume_text = (
                resume_paste.strip()
            )

        job_text = job_paste.strip()

        if not resume_text:
            st.warning(
                "⚠️ CV belum diisi."
            )

        elif not job_text:
            st.warning(
                "⚠️ Job Description wajib diisi."
            )

        else:

            with st.spinner(
                "Menganalisis CV..."
            ):
                try:
                    result = run_analysis(
                        resume_text,
                        job_text,
                    )

                    st.session_state.analysis_result = result
                    st.session_state.resume_text_raw = resume_text
                    st.session_state.job_text_raw = job_text
                    st.session_state.page = "result"

                    st.rerun()

                except Exception as e:
                    st.error(
                        f"Analisis gagal: {e}"
                    )