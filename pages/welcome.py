import streamlit as st


def render():
    st.markdown("""
    <div class="hero">
        <h1>📄 CV Match Analyst</h1>
        <p>Analisis kesesuaian CV dengan Job Description secara otomatis</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Mulai Analisis →", use_container_width=True):
            st.session_state.page = "input"
            st.rerun()
