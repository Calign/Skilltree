import streamlit as st
import pandas as pd


# Load user data
def load_user_data():
    try:
        df = pd.read_excel("user_accounts.xlsx")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["username", "password", "email"])
        df.to_excel("user_accounts.xlsx", index=False)
    return df

# Dummy password hashing function (replace with proper hashing in production)
def hash_password(password):
    return password

def login():
    page_bg_img = """
        <style>
        [data-testid="stAppViewContainer"] {
        background-image: url("https:/img.freepik.com/premium-photo/red-hexagon-connects-majority-structure-others_72572-1792.jpg?w=1060");
        background-size: cover; 
    }

        [data-testid="stHeader"] {
        background-color: rgba(0, 0, 0, 0)
    }
    """ 
    st.markdown(page_bg_img, unsafe_allow_html=True)

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

    # Handle the "logout" action and clear session state
    if 'authenticated' in st.session_state and not st.session_state['authenticated']:
        # If the user is logged out, reset all session data
        st.session_state.clear()

    # Check if the user is authenticated
    if 'authenticated' in st.session_state and st.session_state['authenticated']:
        st.session_state['page'] = 'home'
        st.rerun()

    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/logo.jpg")

    with col2:
        st.header("SkillTree")
        st.title("Login")

        username_input = st.text_input('Username', key="styledinput_username")
        password_input = st.text_input('Password', type='password', key="styledinput_pw")

        # Load user data
        df = load_user_data()

        if st.button('Login'):
            if username_input in df['username'].values:
                user_data = df[df['username'] == username_input].iloc[0]
                if user_data['password'] == password_input:
                    st.success('Login successful!')
                    st.session_state['authenticated'] = True
                    st.session_state['username'] = username_input
                    st.session_state['page'] = 'home'
                    st.rerun()  
                else:
                    st.error('Incorrect password')
            else:
                st.error('Username not found')

        if st.button("I don't have an account"):
            st.session_state['page'] = 'signup'
            st.rerun()
