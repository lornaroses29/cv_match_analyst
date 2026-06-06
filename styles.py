import streamlit as st


def inject_css():
    st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main {
        background-color: #FAFAFA;
    }

    /* ── Hero ── */
    .hero {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border-radius: 16px;
        padding: 48px 32px;
        margin-bottom: 24px;
        text-align: center;
    }
    .hero h1 {
        color: white;
        font-size: 2rem;
        font-weight: 700;
        margin: 0 0 8px 0;
    }
    .hero p {
        font-size: 1rem;
        color: rgba(255,255,255,0.7);
        margin: 0;
    }

    /* ── Page Header ── */
    .page-header { margin-bottom: 24px; }
    .page-header h2 {
        color: white;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0;
    }
    .step-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #6366f1;
        font-weight: 600;
        margin-bottom: 4px;
    }

    /* ── Section Label ── */
    .sec-label {
        font-weight: 600;
        font-size: 0.9rem;
        color: #374151;
        margin-bottom: 8px;
        display: block;
    }

    /* ── Cards ── */
    .card {
        background: white;
        border-radius: 12px;
        padding: 24px;
        border: 1px solid #e5e7eb;
        margin-bottom: 16px;
        height: 75px;
    }
    .card-title {
        font-size: 0.875rem;
        font-weight: 600;
        color: #374151;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 5px;
    }

    /* ── Score Card ── */
    .score-card {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border-radius: 16px;
        padding: 32px;
        text-align: center;
        color: white;
        margin-bottom: 24px;
    }
    .score-number {
        font-size: 4rem;
        font-weight: 700;
        line-height: 1;
        margin-bottom: 8px;
    }
    .score-label {
        font-size: 0.875rem;
        color: rgba(255,255,255,0.7);
        margin-bottom: 16px;
    }
    .score-badge {
        display: inline-block;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    .badge-good { background: #10b981; color: white; }
    .badge-mid  { background: #f59e0b; color: white; }
    .badge-low  { background: #ef4444; color: white; }

    /* ── Progress Bar ── */
    .progress-wrap {
        background: rgba(255,255,255,0.2);
        border-radius: 8px;
        height: 8px;
        width: 100%;
        margin-top: 16px;
        overflow: hidden;
    }
    .progress-fill {
        height: 100%;
        border-radius: 8px;
        background: white;
        transition: width 0.5s ease;
    }

    /* ── Feedback Items ── */
    .feedback-item {
        background: #f8fafc;
        padding: 16px;
        border-radius: 8px;
        margin-bottom: 12px;
        border-left: 3px solid #6366f1;
    }
    .feedback-item strong {
        color: #1e293b;
        display: block;
        margin-bottom: 4px;
    }
    .feedback-item p {
        color: #64748b;
        font-size: 0.875rem;
        margin: 0;
        line-height: 1.5;
    }

    /* ── Recommendation Items ── */
    .rec-item {
        background: #fef3c7;
        padding: 16px;
        border-radius: 8px;
        margin-bottom: 12px;
        border-left: 3px solid #f59e0b;
    }
    .rec-item.success {
        background: #d1fae5;
        border-left-color: #10b981;
    }
    .rec-item strong {
        color: #1e293b;
        display: block;
        margin-bottom: 4px;
    }
    .rec-item p {
        color: #64748b;
        font-size: 0.875rem;
        margin: 0;
        line-height: 1.5;
    }

    /* ── Keywords ── */
    .kw-match {
        display: inline-block;
        background: #d1fae5;
        color: #065f46;
        padding: 4px 10px;
        border-radius: 4px;
        font-size: 0.8rem;
        margin: 3px;
        font-weight: 500;
    }
    .kw-miss {
        display: inline-block;
        background: #fee2e2;
        color: #991b1b;
        padding: 4px 10px;
        border-radius: 4px;
        font-size: 0.8rem;
        margin: 3px;
        font-weight: 500;
    }

    /* ── Job Recommendation Card ── */
    .job-rec-card {
        background: linear-gradient(135deg, #0f766e 0%, #115e59 100%);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 12px;
        color: white;
    }
    .job-rec-card h4 {
        margin: 0 0 8px 0;
        font-size: 1rem;
        font-weight: 600;
    }
    .job-rec-card p {
        margin: 0 0 12px 0;
        font-size: 0.85rem;
        color: rgba(255,255,255,0.8);
        line-height: 1.5;
    }
    .job-rec-skills {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
    }
    .job-rec-skill {
        background: rgba(255,255,255,0.2);
        padding: 4px 10px;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: 500;
    }
    .job-rec-match {
        display: inline-block;
        background: rgba(255,255,255,0.25);
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 0.7rem;
        margin-left: 8px;
        font-weight: 600;
    }

    /* ── Hide Streamlit Chrome ── */
    #MainMenu, footer { visibility: hidden; }
    .stDeployButton { display: none; }

    /* ── Button Override ── */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 600;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    }
</style>
""", unsafe_allow_html=True)
