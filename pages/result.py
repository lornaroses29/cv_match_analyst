import streamlit as st


def render():
    res   = st.session_state.analysis_result
    score = res["score"]
    vc    = res.get("verdict_class", "mid")

    # ── Header ────────────────────────────────────────────────────
    st.markdown("""
    <div class="page-header">
        <div class="step-label">Step 2 of 2 — Hasil</div>
        <h2>Hasil Analisis CV</h2>
    </div>
    """, unsafe_allow_html=True)

    # ── Score Card ────────────────────────────────────────────────
    st.markdown(f"""
    <div class="score-card">
        <div class="score-number">{score}%</div>
        <div class="score-label">Match Score</div>
        <div class="score-badge badge-{vc}">{res['verdict']}</div>
        <div class="progress-wrap">
            <div class="progress-fill" style="width: {score}%"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Feedback ──────────────────────────────────────────────────
    st.markdown("""
    <div class="card">
        <div class="card-title">💡 Feedback</div>
    </div>
    """, unsafe_allow_html=True)

    for fb in res["feedback"]:
        st.markdown(f"""
        <div class="feedback-item">
            <strong>{fb['title']}</strong>
            <p>{fb['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Recommendations ───────────────────────────────────────────
    st.markdown("""
    <div class="card">
        <div class="card-title">🚀 Rekomendasi Perbaikan</div>
    </div>
    """, unsafe_allow_html=True)

    for rec in res["recommendations"]:
        success_class = "success" if rec.get("success", False) else ""
        st.markdown(f"""
        <div class="rec-item {success_class}">
            <strong>{rec['title']}</strong>
            <p>{rec['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Keywords ──────────────────────────────────────────────────
    if res["matched_keywords"] or res["missing_keywords"]:
        st.markdown("""
        <div class="card">
            <div class="card-title">🔑 Analisis Keyword</div>
        </div>
        """, unsafe_allow_html=True)

        if res["matched_keywords"]:
            st.markdown("**Keyword yang Cocok:**")
            kw_html = "".join(f'<span class="kw-match">{k}</span>' for k in res["matched_keywords"])
            st.markdown(kw_html, unsafe_allow_html=True)

        if res["missing_keywords"]:
            st.markdown("**Keyword yang Kurang:**")
            kw_html = "".join(f'<span class="kw-miss">{k}</span>' for k in res["missing_keywords"][:10])
            st.markdown(kw_html, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Job Recommendations ───────────────────────────────────────
    job_recs = res.get("job_recommendations", [])
    if job_recs and vc != "good":
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

    # ── Back Button ───────────────────────────────────────────────
    if st.button("← Analisis Ulang", use_container_width=True):
        st.session_state.page = "input"
        st.rerun()
