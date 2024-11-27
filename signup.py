import streamlit as st
import pandas as pd

try:
    df = pd.read_excel("user_accounts.xlsx")
except FileNotFoundError:
    df = pd.DataFrame(columns=["username", "password", "email", "user_id"])
    df.to_excel("user_accounts.xlsx", index=False)

def hash_password(password):
    return password

def signup():
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
    
    st.header("SkillTree")
    st.title("Sign Up")
    
    username = st.text_input("Choose a Username", key="styledinput_chooseusername")
    password = st.text_input("Choose a Password", type="password", key="styledinput_choosepw")
    email = st.text_input("Email", key="styledinput_email")

    if st.button("Register"):
        if username and password and email:
            if username in df['username'].values or email in df['email'].values:
                st.error("Username or Email already exists.")
            else:
                new_user_id = df['user_id'].max() + 1 if not df.empty else 1

                new_user = pd.DataFrame({
                    "username": [username],
                    "password": [hash_password(password)],
                    "email": [email],
                    "user_id": [new_user_id]
                })

                df_updated = pd.concat([df, new_user], ignore_index=True)

                df_updated.to_excel("user_accounts.xlsx", index=False)

                st.success("Account created! You can now log in.")
                st.session_state['page'] = 'login'
                st.rerun()  
        else:
            st.error("Please fill in all fields.")
    
    if st.button("I already have an account"):
        st.session_state['page'] = 'login'
        st.rerun() 
