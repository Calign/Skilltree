import streamlit as st
from login import login
from signup import signup
from home import home  
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
background-image: url("https://i.pinimg.com/564x/43/6e/cf/436ecf5fd4d20e38df13e72370afdf53.jpg");
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
