import streamlit as st

# Home Page Function
def home():
    button_style = """
        <style>
            .stButton > button {
                background: none !important;
                border: none !important;
                color: #000000;  /* Text color */
                font-size: 16px;  /* Font size */
                font-family: 'Courier New', Courier, monospace;
                cursor: pointer;
                padding: 0;
                text-align: left;
                box-shadow: none !important;  /* Remove any shadow or outline */
            }

            .stButton > button:hover {
                color: #38ef7d;  /* Color when hovered */
                transform: scale(1.05);
                background: none !important;  /* Ensure no background on hover */
            }

            .stButton > button:focus {
                outline: none !important;
                box-shadow: none !important;
            }

        </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    # Custom navigation buttons
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("Home", key="home_button"):
            st.session_state['page'] = 'home'
            st.rerun()

    with col2:
        if st.button("Contact", key="contact_button"):
            st.session_state['page'] = 'contact'
            st.rerun()

    with col3:
        if st.button("Logout", key="logout_button"):
            # Reset session state on logout
            st.session_state['authenticated'] = False  # Clear authentication
            st.session_state['page'] = 'login'  # Set page to login
            st.rerun()  # Rerun to go to the 'login' page

    # Main Content
    st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)

    st.markdown(
        """
        <div>
            <h1>Welcome to SkillTree!</h1>
            <hr style='border: 1px solid black;'/>
            <p class="home-paragraph">SkillTree is designed to help you navigate the path to your ideal career. By taking our aptitude test, you will receive personalized career recommendations tailored to your strengths and skills. Discover new opportunities and uncover potential career paths based on your unique test results. Start your journey today and let SkillTree guide you toward a fulfilling and successful future.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    go_to_test_button = st.button("Go to Test", key="go_to_test_button")

    if go_to_test_button:
        st.session_state['page'] = 'test'
        st.rerun()

