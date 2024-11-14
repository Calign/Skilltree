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

def login():
    st.markdown("""
    <style>
    body {
        background-image: url('https://wallpaperaccess.com/full/188693.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Arial', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

    st.header("SkillTree")
    st.title("Login")

    if 'authenticated' in st.session_state and st.session_state['authenticated']:
        st.session_state['page'] = 'home'
        st.rerun()  # Go to home page if already authenticated
    else:
        username_input = st.text_input('Username', key="styledinput_username")
        password_input = st.text_input('Password', type='password', key="styledinput_pw")

        if st.button('Login'):
            if username_input in df['username'].values:
                user_data = df[df['username'] == username_input].iloc[0]
                if user_data['password'] == password_input:
                    st.success('Login successful!')
                    st.session_state['authenticated'] = True
                    st.session_state['username'] = username_input
                    st.session_state['page'] = 'home'
                    st.rerun()  # Redirect to home page after login
                else:
                    st.error('Incorrect password')
            else:
                st.error('Username not found')

    if st.button("I don't have an account"):
        st.session_state['page'] = 'signup'
        st.rerun()  # Redirect to signup page


