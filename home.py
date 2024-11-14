import pandas as pd
import streamlit as st
from test import test

df = pd.read_excel("test_data.xlsx")

#navigation function
def navigate_to(page_name):
    st.session_state["page"] = page_name
    st.rerun()

#body of the homepage
def home():
    st.title("Home")
    st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)
    st.write("This is the Home Page. Proceed to the Test page when you're ready.")
    if st.button("Go to Test"):
        navigate_to("test")
