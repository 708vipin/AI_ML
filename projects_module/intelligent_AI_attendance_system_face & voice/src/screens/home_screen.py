import streamlit as st

from src.components.header import header_home
from src.ui.base_layout import style_base_layout
from src.ui.base_layout import style_background_home


def home_screen():
  

    header_home()

    style_base_layout()

    style_background_home()

    


    col1, col2 = st.columns(2)

    with col1:
        st.header("I'm Teacher")
        st.image("https://github.com/shradha-khapra/ai-attendance-project-landing/blob/main/static/img/demo/snap-teacher.png")
        if st.button("Teacher portal"):
            st.session_state['login_type']='teacher'
            st.rerun()

    with col2:
        st.header("I'm student")
        if st.button("Student portal"):
            st.session_state['login_type']='student'
            st.rerun()