import pandas as pd
import re
import hashlib


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


def login(username, email, password):
    all_data = ""
    try:
        all_data = load_all_data()
    except:
        pass

    print("Dataframe")
    print(all_data)

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # convert username to string, so that even if the user enters a number, it can be compared
    all_data["username"] = all_data["username"].astype(str)  # type:ignore

    # TODO: remove this line, as email will be string only.
    all_data["email"] = all_data["email"].astype(str)  # type:ignore

    user = all_data[  # type:ignore
        (all_data["username"] == username)  # type:ignore
        & (all_data["password"] == hashed_password)  # type:ignore
        & (all_data["email"] == email)  # type:ignore
    ]

    if not user.empty:  # type:ignore
        return True
    else:
        return False
