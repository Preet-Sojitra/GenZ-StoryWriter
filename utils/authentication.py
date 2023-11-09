import pandas as pd
import re


def load_all_data():
    try:
        all_data = pd.read_csv("userCredentials.csv")
        return all_data
    except FileNotFoundError:
        # If the file doesn't exist yet, return an empty DataFrame with the correct columns
        return pd.DataFrame(columns=["username", "email", "password"])


# Save user data to CSV
def save_user_data(user_data):
    user_data.to_csv("userCredentials.csv", index=False)


def is_valid_username(username):
    return re.match("^[a-zA-Z0-9]+$", username) is not None


def is_strong_password(password):
    return (
        len(password) >= 8
        and any(c.isalpha() for c in password)
        and any(c.isdigit() for c in password)
    )
