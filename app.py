from config import setup_page, init_session_state, download_nltk_resources
from styles import inject_css

import streamlit as st
from pages import welcome, input, result

# ── Bootstrap ─────────────────────────────────────────────────────────
setup_page()
init_session_state()
download_nltk_resources()
inject_css()

# ── Router ────────────────────────────────────────────────────────────
PAGE_MAP = {
    "welcome": welcome.render,
    "input":   input.render,
    "result":  result.render,
}

renderer = PAGE_MAP.get(st.session_state.page)
if renderer:
    renderer()
