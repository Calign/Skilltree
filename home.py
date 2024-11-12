import pandas as pd
import streamlit as st
from test import test

# Load the Excel file
df = pd.read_excel("test_data.xlsx")

# Dictionary to store user responses
def navigate_to(page_name):
    st.session_state["page"] = page_name
    st.rerun()

def home():
    st.title("Home Page 124134")
    st.write("This is the Home Page. Proceed to the Test page when you're ready.")
    if st.button("Go to Test"):
        navigate_to("test")
