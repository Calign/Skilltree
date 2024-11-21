import streamlit as st


def contact():
    button_style = """
        <style>
            /* Remove the default button background and borders */
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

            /* Hover effect to change the text color */
            .stButton > button:hover {
                color: #38ef7d;  /* Color when hovered */
                transform: scale(1.05);
                background: none !important;  /* Ensure no background on hover */
            }

            /* Ensure there's no outline or border when focused */
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
        if st.button("🏠Home", key="home_button"):
            st.session_state['page'] = 'home'
            st.rerun()

    with col2:
        if st.button("📱Contact", key="contact_button"):
            st.session_state['page'] = 'contact'
            st.rerun()

    with col3:
        if st.button("⭕Logout", key="logout_button"):
            st.session_state['page'] = 'login'
            st.rerun()
    st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)

        
    st.title("Contact Us")
    st.markdown(
        """
        <div>
        <p class="contact-paragraph">If you have any inquiries, you may send us a message, and we will be in touch as soon as possible. Thank you!</p>

        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.subheader("Contact Details")
    
    st.markdown(
        """
        **Zandro Alvaro B. Caling**  
        📧 czb0177@dlsud.edu.ph  

        **John Gabriel A. Alcedo**  
        📧 aja2107@dlsud.edu.ph
        """
    )
    
    