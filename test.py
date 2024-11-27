import pandas as pd
import random
import streamlit as st
import pathlib

# Load the test data
df = pd.read_excel("test_data.xlsx")  # Ensure this file exists with the specified columns

# Initialize session state for tracking scores and progress
if "scores" not in st.session_state:
    st.session_state.scores = {
        "English": None,
        "Math": None,
        "History": None,
        "Science": None,
        "Filipino": None,
    }

if "current_subject" not in st.session_state:
    st.session_state.current_subject = None

if "answered_subjects" not in st.session_state:
    st.session_state.answered_subjects = set()

if "current_questions" not in st.session_state:
    st.session_state.current_questions = []

if "cancel_test" not in st.session_state:
    st.session_state.cancel_test = False

def cancel_test():
    """Reset all session state variables to cancel the test."""
    st.session_state.scores = {key: None for key in st.session_state.scores.keys()}
    st.session_state.answered_subjects = set()
    st.session_state.current_subject = None
    st.session_state.current_questions = []
    st.session_state.cancel_test = True
    st.session_state['page'] = 'home'
    st.rerun()

def calculate_percentage(score, total):
    page_bg_img = """
        <style>
        [data-testid="stAppViewContainer"] {
        background-image: url("https://img.freepik.com/free-photo/3d-background-with-white-cubes_23-2150472987.jpg?t=st=1732636928~exp=1732640528~hmac=5d904953436e04c32e67a18758176db9970c5c39108a6a98dde8a2c58d710b40&w=1060");
        background-size: cover;
    }

        [data-testid="stHeader"] {
        background-color: rgba(0, 0, 0, 0)
        }
    """ 
    st.markdown(page_bg_img, unsafe_allow_html=True)

    """Calculate the percentage of the user's score."""
    return round((score / total) * 100, 2)

def display_questions(subject):
    """Display a randomized 10-question test for the selected subject."""
    st.subheader(f"{subject} Test")

    # Filter questions for the selected subject
    subject_data = df[df["Subject"] == subject]
    
    # Separate questions by points
    one_point_questions = subject_data[subject_data["Score"] == 1]
    three_point_questions = subject_data[subject_data["Score"] == 3]
    five_point_questions = subject_data[subject_data["Score"] == 5]
    
    # List to store selected questions
    selected_questions = []
    total_points = 0

    # Keep selecting questions until the total points are exactly 10
    while total_points != 10:
        # Randomly pick questions from any category
        question_pool = pd.concat([one_point_questions, three_point_questions, five_point_questions])
        random_question = question_pool.sample(1).iloc[0]  # Randomly select a question

        if total_points + random_question["Score"] <= 10:
            selected_questions.append(random_question)
            total_points += random_question["Score"]

    st.session_state.current_questions = selected_questions

    user_score = 0
    for i, question in enumerate(st.session_state.current_questions):
        st.write(f"Q{i + 1}: {question['Question']}")
        st.write(f"Points: {question['Score']}")

        # Display the answer options
        options = {
            "A": question["A"],
            "B": question["B"],
            "C": question["C"],
            "D": question["D"],
        }

        # Use the keys of `options` for the radio choices
        answer = st.radio(
            f"Choose the correct answer for Q{i + 1}:",
            options=list(options.keys()),
            format_func=lambda x: f"{x}: {options[x]}",  # Display choices with their descriptions
            key=f"{subject}_q{i}",
        )

        # Check if the selected answer matches the correct one
        if answer == question["Answer"]:
            user_score += question["Score"]

    if st.button("Submit Test"):
        st.session_state.scores[subject] = user_score
        st.session_state.answered_subjects.add(subject)
        st.session_state.current_subject = None
        st.session_state.current_questions = []
        st.rerun()


def display_selection():
    page_bg_img = """
        <style>
        [data-testid="stAppViewContainer"] {
        background-image: url("https://img.freepik.com/free-photo/3d-background-with-white-cubes_23-2150472987.jpg?t=st=1732636928~exp=1732640528~hmac=5d904953436e04c32e67a18758176db9970c5c39108a6a98dde8a2c58d710b40&w=1060");
        background-size: cover;
    }

        [data-testid="stHeader"] {
        background-color: rgba(0, 0, 0, 0)
        }
    """ 
    st.markdown(page_bg_img, unsafe_allow_html=True)

    """Display the main test selection screen."""
    st.title("Bachelor Degree Aptitude Test")
    st.write("""<hr style='border: 1px solid black;' />
             \nInstructions: The test consists of five subjects:
             \n• English 
             \n• Math 
             \n• History 
             \n• Science 
             \n• Filipino
             \nEach subject consist of 10 iterm test overall wth variety of points based on the difficulty of questions.
             <hr style='border: 1px solid black;' />
             \nHow the Test Works:
             \n• select any of the subjects to begin the test. All questions are randomize each take of test
             \n• If you cancel or skip the test, your progress will be reset, and you can start over.
             \n• Once you have answered all the questions for a subject, you can click on the Submit Test button to submit your answers.
             \n• If you fail two or more subjects, you will be prompted to retake the test.
             \n• Your score for that subject will be recorded and you may not return to retake that subject unless you choose to cancel the test or retake the take after failing the attempt
             \n Goodluck!
             <hr style='border: 1px solid black;' />
             \n• All questions are in multiple choice test type and you will be presented with 4 options (A, B, C, D). Select the correct answer.
             \n Select a subject to take the test: 
""", unsafe_allow_html=True)


    col1, col2, col3, col4, col5 = st.columns(5)

    # Buttons for each subject
    with col1:
        if st.button("English", disabled="English" in st.session_state.answered_subjects):
            st.session_state.current_subject = "English"
    with col2:
        if st.button("Math", disabled="Math" in st.session_state.answered_subjects):
            st.session_state.current_subject = "Math"
    with col3:
        if st.button("History", disabled="History" in st.session_state.answered_subjects):
            st.session_state.current_subject = "History"
    with col4:
        if st.button("Science", disabled="Science" in st.session_state.answered_subjects):
            st.session_state.current_subject = "Science"
    with col5:
        if st.button("Filipino", disabled="Filipino" in st.session_state.answered_subjects):
            st.session_state.current_subject = "Filipino"

    # Add "Test run skip" button
    if st.button("Test run skip"):
        st.session_state.scores = {
            "English": 6,   # Example predetermined scores
            "Math": 10,
            "History": 8,
            "Science": 9,
            "Filipino": 7,
        }
        st.session_state.answered_subjects = set(st.session_state.scores.keys())
        st.write("Scores set for test run:")
        for subject, score in st.session_state.scores.items():
            st.write(f"{subject}: {score}/10")
        # Navigate to results
        st.session_state.current_subject = None
        st.session_state["page"] = "result"
        st.rerun()  # Redirect to results

    # Cancel test button
    st.markdown("<hr style='border: 1px solid black;' />", unsafe_allow_html=True)
    if st.button("Cancel Test"):
        cancel_test()
        st.warning("Test attempt has been canceled. All scores reset.")

    # Display current scores and completion status
    st.write("Your Scores:")
    scores_exist = any(score is not None for score in st.session_state.scores.values())

    if scores_exist:
        for subject, score in st.session_state.scores.items():
            if score is not None:
                percentage = calculate_percentage(score, 10)
                st.write(f"{subject}: {score}/10 ({percentage}%)")
    else:
        st.write("No scores recorded yet. Take a test to see your progress!")

def final_results():
    """Display final results and handle pass/fail logic."""
    st.subheader("Final Results")
    failed_subjects = [subject for subject, score in st.session_state.scores.items() if calculate_percentage(score, 10) < 50]

    if len(failed_subjects) >= 2:
        st.error("You have failed the test")
        st.write("""If you'd like to try again, click below to retake the test and show us how much you've improved!

""", unsafe_allow_html=True)
        if st.button("Retake Test"):
            # Reset all session state variables
            st.session_state.scores = {key: None for key in st.session_state.scores.keys()}
            st.session_state.answered_subjects = set()
            st.session_state.current_subject = None
            st.session_state.current_questions = []
            st.rerun()  # Refresh the app to restart the test
        st.subheader("or")
        if st.button("Go back to home"):
            st.session_state.scores = {key: None for key in st.session_state.scores.keys()}
            st.session_state.answered_subjects = set()
            st.session_state.current_subject = None
            st.session_state.current_questions = []
            st.session_state['page'] = 'home'
            st.rerun()
        st.write("""Don't worry! Everyone faces challenges, and failure is just part of the learning process. Use this as an opportunity to focus on areas that need improvement
""", unsafe_allow_html=True)
    
        st.image('https://i.pinimg.com/originals/e7/fb/06/e7fb06e185abb65900e4344a3d715751.png', width=700)
    else:
        st.success("Congratulations! You passed the test.")
        # Save results to result.py
        with open("result.py", "w") as f:
            f.write(f"results = {st.session_state.scores}")
        st.write("Results saved to result.py")

def test():
    """Main function to manage the test workflow."""
    if all(subject in st.session_state.answered_subjects for subject in st.session_state.scores.keys()):
        final_results()
    elif st.session_state.current_subject:
        display_questions(st.session_state.current_subject)
    else:
        display_selection()
