import streamlit as st
import pandas as pd

# Load user data
try:
    df = pd.read_excel("user_accounts.xlsx")
except FileNotFoundError:
    df = pd.DataFrame(columns=["username", "password", "email"])
    df.to_excel("user_accounts.xlsx", index=False)

# Dummy password hashing function (replace with proper hashing in production)
def hash_password(password):
    return password

def signup():
    st.title("Sign Up")
    username = st.text_input("Choose a Username", key="styledinput_chooseusername")
    password = st.text_input("Choose a Password", type="password", key="styledinput_choosepw")
    email = st.text_input("Email", key="styledinput_email")

    if st.button("Register", key="button"):
        if username and password and email:
            if username in df['username'].values or email in df['email'].values:
                st.error("Username or Email already exists.")
            else:
                new_user = pd.DataFrame({
                    "username": [username],
                    "password": [hash_password(password)],
                    "email": [email]
                })
                df_updated = pd.concat([df, new_user], ignore_index=True)
                df_updated.to_excel("user_accounts.xlsx", index=False)
                st.success("Account created! You can now log in.")
                st.session_state['page'] = 'login'
                st.rerun()  # Redirect to login page after signup
        else:
            st.error("Please fill in all fields.")
    
    if st.button("I already have an account", key="button_green"):
        st.session_state['page'] = 'login'
        st.rerun()  # Redirect to login page
