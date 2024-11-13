import pandas as pd
import streamlit as st

# Load the Excel file
df = pd.read_excel("test_data.xlsx")

# Dictionary to store user responses
user_answers = {}

def test():
    st.title("Bachelor Degree Aptitude Test")
    
    for index, row in df.iterrows():
        st.write(f"**{row['Question']}**")
        
        # Display options for each question
        user_answers[row['Subject_ID']] = st.radio(
            f"Select your answer for {row['Subject']}:",
            options=["A", "B", "C", "D"],
            format_func=lambda x: row[x],
            key=row['Subject_ID']
        )

    # Submit button
    if st.button("Submit",key="button"):
        subject_scores = {subject: 0 for subject in df['Subject'].unique()}

        # Calculate scores
        for index, row in df.iterrows():
            question_id = row["Subject_ID"]
            subject = row["Subject"]
            correct_answer = row["Answer"]
            score_value = row["Score"]

            if user_answers.get(question_id) == correct_answer:
                subject_scores[subject] += score_value

        # Store subject_scores in session state to access it in the result page
        st.session_state['subject_scores'] = subject_scores
        st.session_state['page'] = 'result'
        st.rerun()
