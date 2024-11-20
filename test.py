import pandas as pd
import streamlit as st

# Load the test data
df = pd.read_excel("test_data.xlsx")

# Store user's responses
user_answers = {}

def test():
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background: url(https://img.freepik.com/premium-photo/abstract-white-bluish-background_921860-18613.jpg);
    background-size: cover;
    }

    [data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0)
    }
    """ 
    st.markdown(page_bg_img, unsafe_allow_html=True)


    st.title("Bachelor Degree Aptitude Test")
    st.subheader("Instructions: Read each question carefully and select the option for the correct answer.")

    # Display subjects and their scores
    subjects = df['Subject'].unique()
    
    # Create a dictionary to store scores for each subject
    subject_scores = {subject: 0 for subject in subjects}

    # Display the subject once
    for subject in subjects:
        # Use markdown to align the subject name to the right
        st.markdown(f"<h3 style='text-align: left;'>{subject}</h3>", unsafe_allow_html=True)

        # Filter questions related to the subject
        subject_questions = df[df['Subject'] == subject]

        # Display questions for each subject
        for idx, (index, row) in enumerate(subject_questions.iterrows(), start=1):
            st.write(f"**{idx}. {row['Question']}**")
            
            # Display the options for each question with Subject_ID
            user_answers[row['Subject_ID']] = st.radio(
                f"Select your answer for {row['Subject_ID']}:",
                options=["A", "B", "C", "D"],
                format_func=lambda x: row[x],
                key=row['Subject_ID']
            )

    # Submit button
    if st.button("Submit"):
        # Calculate scores based on answers
        for index, row in df.iterrows():
            question_id = row["Subject_ID"]
            subject = row["Subject"]
            correct_answer = row["Answer"]
            score_value = row["Score"]

            if user_answers.get(question_id) == correct_answer:
                subject_scores[subject] += score_value

        # Ensure total score doesn't exceed 25 points for each subject
        for subject in subject_scores:
            subject_scores[subject] = min(subject_scores[subject], 25)

        # Store the user scores in session state
        st.session_state['subject_scores'] = subject_scores
        st.session_state['page'] = 'result'
        st.rerun()
