import streamlit as st
from login import login
from signup import signup
from home import home  
from contact import contact
from test import test
from result import result
import pathlib

def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

css_path = pathlib.Path("assets/styles.css")
load_css(css_path)

#app background
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://img.freepik.com/free-photo/3d-background-with-white-cubes_23-2150472987.jpg?t=st=1732636928~exp=1732640528~hmac=5d904953436e04c32e67a18758176db9970c5c39108a6a98dde8a2c58d710b40&w=1060");
background-size: cover;
}

[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0)
}
""" 
st.markdown(page_bg_img, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state['page'] = 'login'

# Main Page Navigation
if st.session_state['page'] == 'login':
    login()
elif st.session_state['page'] == 'signup':
    signup()
elif st.session_state['page'] == 'home':
    home()
elif st.session_state['page'] == 'test':
    test()
elif st.session_state['page'] == 'result':
    result()
elif st.session_state['page'] == 'contact':
    contact()
