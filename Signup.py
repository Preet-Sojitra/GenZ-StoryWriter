import hashlib
import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from utils.authentication import *

if "header_added" not in st.session_state:
    st.session_state.header_added = False

st.set_page_config(page_title="Signup Page", page_icon=":lock:")

st.sidebar.success("Signup Page")

st.title("Signup Page")
st.write("Please enter your details to sign up.")

data = []
header = ["username", "email", "password"]
l = []

# Check if the header has already been added
if not st.session_state.header_added:
    data.append(header)
    st.session_state.header_added = True


# Input fields for signup
username = str(st.text_input("Username: "))
email = str(st.text_input("Email: "))
password = st.text_input("Password: ", type="password")

all_data = ""
try:
    all_data = load_all_data()
except:
    pass

# print(all_data)
# print(type(all_data))


if st.button("Sign Up"):
    if not is_valid_username(username):
        st.error("Username must be alpha-numeric.")
    elif not is_strong_password(password):
        st.error(
            "Password must be at least 8 characters long and contain both letters and numbers."
        )
    elif not all_data[all_data["username"] == username].empty:  # type: ignore
        st.error("Username already taken. Please choose another one.")
    else:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        new_user = pd.DataFrame(
            {
                "username": [str(username)],
                "email": [str(email)],
                "password": [hashed_password],
            }
        )
        user_data = pd.concat([all_data, new_user], ignore_index=True)  # type:ignore
        save_user_data(user_data)
        st.success("Sign-up successful! You can now login.")

        # Redirect to login page
        # switch_page("Login")
