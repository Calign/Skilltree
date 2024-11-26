import streamlit as st
from streamlit_option_menu import option_menu


def contact():

    nav_bar = option_menu(
        None, ["Home", "Contact Us", "Logout"],
        icons=["house", "envelope", "box-arrow-right"],
        menu_icon="cast", default_index=0, orientation="horizontal"
    )
    
    # Navigation Actions
    if nav_bar == 'Home' and st.session_state.get('page') != 'home':
        st.session_state["page"] = "home"
        st.rerun()
    elif nav_bar == 'Contact Us' and st.session_state.get('page') != 'contact':
        st.session_state["page"] = "contact"
        st.rerun()
    elif nav_bar == 'Logout' and st.session_state.get('page') != 'login':
        st.session_state["page"] = "login"
        st.session_state.clear()
        st.rerun()

        
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
    
    