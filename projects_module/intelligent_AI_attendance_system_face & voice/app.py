import streamlit as st


def main():
    st.header("This is title")
    name = st.text_input("enter your name")
    
    col1, col2 = st.columns(2, gap ="small")

    with col1:
      if st.button("Display my name", key="btn1", type="primary", width="content"):
        print("hi", name)
    
    with col2:
      if st.button("Display my name", key="btn2", type="primary", width="content"):
        print("bye", name)

main()    