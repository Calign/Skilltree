import streamlit as st
from login import login
from signup import signup
from home import home  
from test import test
from result import result

if 'page' not in st.session_state:
    st.session_state['page'] = 'login'

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
