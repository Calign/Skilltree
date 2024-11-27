import streamlit as st
from streamlit_option_menu import option_menu

# Home Page Function
def home():
    # Navigation Bar
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
        st.session_state["authenticated"] = False
        st.session_state["page"] = "login"
        st.rerun()

    st.markdown("<h1>Welcome to SkillTree!</h1>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.write("""SkillTree is designed to help you navigate the path to your ideal career. By taking our aptitude test, you will receive personalized career recommendations tailored to your strengths and skills. Discover new nopportunities and uncover potential career paths based on your unique test results. Start your journey 
             ntoday and let SkillTree guide you toward a fulfilling and successful future.
""",  unsafe_allow_html=True)
    st.write()
    st.write("""Select the test start button below to start taking the test and answer the questions. Once you've completed the test, review your results, explore recommended degrees, and see where your skills can take you!
             \n<hr style='border: 1px solid black;'/>
""", unsafe_allow_html=True)


    # Navigation Button to Test
    
    if st.button("Test Start"):
        st.session_state["page"] = "test"
        st.rerun()
    
    
    st.write("""Why Take This Test?
             \n• Understand your academic strengths: Find out which subjects you're excelling in.
             \n• Get degree recommendations: Based on your scores, the app recommends top 5 bachelor degree programs that align with your academic profile.
             \n• Prepare for the future: Whether you're choosing your degree or preparing for college entrance exams, this software will give you valuable insights into your potential.
""", unsafe_allow_html=True)
