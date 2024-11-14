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
    st.header("SkillTree")
    st.markdown(
        """
        <div>
            <h1>Welcome to SkillTree!</h1>
            <hr style='border: 1px solid black;'>
            <p class="home-paragraph">SkillTree is designed to help you navigate the path to your ideal career. By taking our aptitude test, you will receive personalized career recommendations tailored to your strengths and skills. Discover new opportunities and uncover potential career paths based on your unique test results. Start your journey today and let SkillTree guide you toward a fulfilling and successful future.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Go to Test"):
        navigate_to("test")
