import streamlit as st
import hashlib

import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from utils.logging_util import CustomLogger

st.sidebar.success("Login Page")


def load_all_data():
    try:
        all_data = pd.read_csv("userCredentials.csv")
        return all_data
    except FileNotFoundError:
        # all_data = pd.DataFrame(columns=header)
        pass


def load_user_credentials():
    df = pd.read_csv("userCredentials.csv")
    return df


st.title("Login Page")

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

user_credentials_df = load_user_credentials()

all_data = ""
try:
    all_data = load_all_data()
except:
    pass

print(all_data)


def login(username, email, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    user = all_data[  # type:ignore
        (all_data["username"] == username)  # type:ignore
        & (all_data["password"] == hashed_password)  # type:ignore
        & (all_data["email"] == email)  # type:ignore
    ]

    if not user.empty:  # type:ignore
        st.success("Login successful!")
        return True
    else:
        st.error("Login failed. Please check your credentials.")
        return False

    # match the username, email and password for the user
    # index = user_credentials_df.index[
    #     user_credentials_df["username"] == username
    # ].tolist()

    # correct_username = user_credentials_df["username"][index[0]]
    # correct_email = user_credentials_df["email"][index[0]]
    # correct_password = user_credentials_df["password"][index[0]]

    # if (
    #     username == correct_username
    #     and email == correct_email
    #     and password == str(correct_password)
    # ):
    #     return True
    # else:
    #     return False


if st.button("Login"):
    if login(username, email, password):
        # st.success("Login successful!")
        logger = CustomLogger()
        logger.log(f"User-{username} logged in")
        switch_page("GenZ_Story_Writer")
    # else:
    #     st.error("Login failed. Please check your credentials.")
