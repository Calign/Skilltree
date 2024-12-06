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

def hash_password(password):
    return password 

def login():
    # Background styling
    page_bg_img = """
        <style>
        [data-testid="stAppViewContainer"] {
            background-image: url("https://img.freepik.com/premium-photo/red-hexagon-connects-majority-structure-others_72572-1792.jpg?w=1060");
            background-size: cover;
        }
        [data-testid="stHeader"] {
            background-color: rgba(0, 0, 0, 0);
        }
        </style>
    """ 
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Check if user is already authenticated
    if st.session_state.get("authenticated", False):
        st.session_state["page"] = "home"
        st.rerun()

    # Login form layout
    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/logo.jpg", use_column_width=True)

    with col2:
        st.header("SkillTree")
        st.title("Login")

        # User input fields
        username_input = st.text_input("Username", key="styledinput_username")
        password_input = st.text_input("Password", type="password", key="styledinput_pw")

        # Load user data
        df = load_user_data()

        # Login button logic
        if st.button("Login"):
            if username_input in df["username"].values:
                user_data = df[df["username"] == username_input].iloc[0]
                if user_data["password"] == hash_password(password_input):
                    st.success("Login successful!")
                    st.session_state["authenticated"] = True
                    st.session_state["username"] = username_input
                    st.session_state["page"] = "home"
                    st.rerun() 
                else:
                    st.error("Incorrect password")
            else:
                st.error("Username not found")

        # Signup redirection
        if st.button("I don't have an account"):
            st.session_state["page"] = "signup"
            st.rerun()
