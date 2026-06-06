import streamlit as st
import nltk


def setup_page():
    st.set_page_config(
        page_title="CV Match Analyst",
        page_icon="📄",
        layout="centered",
        initial_sidebar_state="collapsed",
    )


def init_session_state():
    defaults = {
        "page": "welcome",
        "analysis_result": None,
        "resume_text_raw": "",
        "job_text_raw": "",
    }
    for key, default in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default


@st.cache_resource
def download_nltk_resources():
    nltk.download("punkt", quiet=True)
    nltk.download("punkt_tab", quiet=True)
    nltk.download("stopwords", quiet=True)
    nltk.download("averaged_perceptron_tagger", quiet=True)
    nltk.download("averaged_perceptron_tagger_eng", quiet=True)
    nltk.download("wordnet", quiet=True)
