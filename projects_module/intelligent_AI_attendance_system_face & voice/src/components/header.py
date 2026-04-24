import streamlit as st


def header_home():

    logo_url = r"C:\Users\pvipi\Desktop\VIP_GitHub\AI_ML\projects_module\intelligent_AI_attendance_system_face & voice\images\logo.png"
    
    st.markdown(f"""

                <div>
              <img src='{logo_url}' height:100px; />
              </div>
              
              
              """, unsafe_allow_html = True)