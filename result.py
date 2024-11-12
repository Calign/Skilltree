import streamlit as st 

def result():
    st.title("Test Results")
    
    # Retrieve scores from session state
    subject_scores = st.session_state.get('subject_scores', {})
    
    if subject_scores:
        st.write("### Your Scores by Subject")
        for subject, score in subject_scores.items():
            st.write(f"**{subject} Score:** {score}")
    else:
        st.write("No scores available. Please complete the test first.")
    
    # Option to go back to the main or home page if needed
    if st.button("Back to Home"):
        st.session_state['page'] = 'home'
        st.rerun()
