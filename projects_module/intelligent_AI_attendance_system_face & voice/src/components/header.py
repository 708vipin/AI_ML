import streamlit as st


def header_home():

    logo_url = r"https://github.com/shradha-khapra/ai-attendance-project-landing/blob/main/static/img/logo.png?raw=true" 
    
    st.markdown(f"""

                <div>
              <img src='{logo_url}' style = "height:100px;" />
              </div>
              
              
              """, unsafe_allow_html = True)