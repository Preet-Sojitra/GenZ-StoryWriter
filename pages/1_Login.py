import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from utils.authentication import login

st.sidebar.success("Login Page")
st.title("Login Page")


username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if login(username, email, password):
        # st.success("Login successful!")
        switch_page("GenZ_Story_Writer")
    else:
        st.error("Login failed. Please check your credentials.")
