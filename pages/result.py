import streamlit as st


def render():

    res = st.session_state.get("analysis_result")

    if not res:
        st.warning("Belum ada hasil analisis.")
        return

    score = res.get("score", 0)
    vc = res.get("verdict_class", "mid")

    matched = res.get("matched_keywords", [])
    missing = res.get("missing_keywords", [])
    job_recs = res.get("job_recommendations", [])

    progress_width = max(score, 5)

    # ==========================================
    # Header
    # ==========================================
    st.markdown("""
    <div class="page-header">
        <div class="step-label">
            Step 2 of 2 — Hasil
        </div>
        <h2>Hasil Analisis CV</h2>
    </div>
    """, unsafe_allow_html=True)

    # ==========================================
    # Score Card
    # ==========================================
    st.markdown(f"""
    <div class="score-card">
        <div class="score-number">{score}%</div>
        <div class="score-label">Match Score</div>
        <div class="score-badge badge-{vc}">
            {res.get('verdict', '-')}
        </div>
    </div>
    """, unsafe_allow_html=True)

    progress_html = f"""
    <div class="progress-wrap">
        <div class="progress-fill"
            style="width:{progress_width}%;">
        </div>
    </div>
    """

    st.markdown(progress_html, unsafe_allow_html=True)

    # ==========================================
    # Metrics
    # ==========================================
    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Match Score",
            f"{score}%"
        )

    with c2:
        st.metric(
            "Keyword Cocok",
            len(matched)
        )

    with c3:
        st.metric(
            "Keyword Kurang",
            len(missing)
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================================
    # Feedback
    # ==========================================
    st.markdown("""
    <div class="card">
        <div class="card-title">
            💡 Feedback
        </div>
    </div>
    """, unsafe_allow_html=True)

    for fb in res.get("feedback", []):

        st.markdown(f"""
        <div class="feedback-item">
            <strong>{fb.get('title', '')}</strong>
            <p>{fb.get('desc', '')}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================================
    # Recommendations
    # ==========================================
    st.markdown("""
    <div class="card">
        <div class="card-title">
            🚀 Rekomendasi Perbaikan
        </div>
    </div>
    """, unsafe_allow_html=True)

    for rec in res.get("recommendations", []):

        success_class = (
            "success"
            if rec.get("success", False)
            else ""
        )

        st.markdown(f"""
        <div class="rec-item {success_class}">
            <strong>{rec.get('title', '')}</strong>
            <p>{rec.get('desc', '')}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================================
    # Keywords
    # ==========================================
    if matched or missing:

        st.markdown("""
        <div class="card">
            <div class="card-title">
                🔑 Analisis Keyword
            </div>
        </div>
        """, unsafe_allow_html=True)

        if matched:

            st.markdown(
                "**Keyword yang Cocok:**"
            )

            kw_html = "".join(
                f'<span class="kw-match">{k}</span>'
                for k in sorted(matched)
            )

            st.markdown(
                kw_html,
                unsafe_allow_html=True
            )

        if missing:

            st.markdown(
                "**Keyword yang Kurang:**"
            )

            kw_html = "".join(
                f'<span class="kw-miss">{k}</span>'
                for k in sorted(missing[:10])
            )

            st.markdown(
                kw_html,
                unsafe_allow_html=True
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================================
    # Alternative Job Recommendations
    # ==========================================
    job_recs = res.get("job_recommendations", [])
    if job_recs and score < 60:
        st.markdown("""
        <div class="card">
            <div class="card-title">Rekomendasi Posisi Lain</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <p style="color: #64748b; font-size: 0.875rem; margin-bottom: 16px;">
            Berdasarkan skill di CV kamu, posisi berikut mungkin lebih cocok:
        </p>
        """, unsafe_allow_html=True)

        for job in job_recs:
            skills_html = "".join(f'<span class="job-rec-skill">{s}</span>' for s in job["matched_skills"])
            st.markdown(f"""
            <div class="job-rec-card">
                <h4>{job['title']} <span class="job-rec-match">{job['match_score']}% match</span></h4>
                <p>{job['description']}</p>
                <div class="job-rec-skills">{skills_html}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    # ==========================================
    # Button
    # ==========================================
    if st.button(
        "← Analisis Ulang",
        use_container_width=True
    ):
        st.session_state.page = "input"
        st.rerun()