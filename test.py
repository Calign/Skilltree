import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_excel("test_data.xlsx")  

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

def knapsack_dp(subject_data, max_points=10):
    """Select questions optimally to sum up to max_points."""
    n = len(subject_data)
    dp = [[0] * (max_points + 1) for _ in range(n + 1)] 
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, max_points + 1):
            if subject_data.iloc[i - 1]["Score"] <= w:
                # Update this cell by considering the question score (not just +1)
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - subject_data.iloc[i - 1]["Score"]] + subject_data.iloc[i - 1]["Score"])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Reconstruct the selected questions from the DP table
    selected_questions = []
    w = max_points
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_questions.append(subject_data.iloc[i - 1])
            w -= subject_data.iloc[i - 1]["Score"]

    return selected_questions

def display_questions(subject):
    st.subheader(f"{subject} Test")

    # Only generate questions if not already stored
    if not st.session_state.current_questions:
        # Filter questions for the selected subject
        subject_data = df[df["Subject"] == subject]
        
        selected_questions = knapsack_dp(subject_data)
        
        st.session_state.current_questions = selected_questions

    # Retrieve stored questions and display them
    user_score = 0
    for i, question in enumerate(st.session_state.current_questions):
        st.write(f"Q{i + 1}: {question['Question']}")
        st.write(f"Points: {question['Score']}")

        options = {
            "A": question["A"],
            "B": question["B"],
            "C": question["C"],
            "D": question["D"],
        }

        answer = st.radio(
            f"Choose the correct answer for Q{i + 1}:",
            options=list(options.keys()),
            format_func=lambda x: f"{x}: {options[x]}",
            key=f"{subject}_q{i}",
        )

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

    st.title("Bachelor Degree Aptitude Test")
    st.write("""<hr style='border: 1px solid black;' />
             \nInstructions: The test consists of five subjects:
             \n• English 
             \n• Math 
             \n• History 
             \n• Science 
             \n• Filipino
             \nEach subject consist of 10 item test overall with a variety of points based on the difficulty of questions.
             <hr style='border: 1px solid black;' />
             \nHow the Test Works:
             \n• Select any of the subjects to begin the test. All questions are randomized for each test
             \n• If you cancel or skip the test, your progress will be reset, and you can start over.
             \n• Once you have answered all the questions for a subject, you can click on the Submit Test button to submit your answers.
             \n• Passing Score for all subjects is 60%.
             \n• If you fail two or more subjects, you will be prompted to retake the test.
             \n• Your score for that subject will be recorded and you may not return to retake that subject unless you choose to cancel the test or retake the test after failing the attempt.
             \n Good luck!
             <hr style='border: 1px solid black;' />
             \n• All questions are in multiple choice test format. You will be presented with 4 options (A, B, C, D). Select the correct answer.
             \n Select a subject to take the test: 
""", unsafe_allow_html=True)


    col1, col2, col3, col4, col5 = st.columns(5)

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

    # For beta testing purpose
    if st.button("Test run skip"):
        st.session_state.scores = {
            "English": 6,   
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
        st.rerun()  

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
    st.error("You have failed the test.")
    failed_subjects = [subject for subject, score in st.session_state.scores.items() if calculate_percentage(score, 10) < 60]

    # Show user's scores in text form and calculate the total score
    st.subheader("Your Scores:")
    st.markdown("<hr style='border: 1px solid black;' />", unsafe_allow_html=True)
    total_score = 0  
    num_correct = 0  
    num_incorrect = 0
    col1, col2 = st.columns(2)

    with col1: 
        for subject, score in st.session_state.scores.items():
            if score is not None:
                percentage = calculate_percentage(score, 10)
                pass_fail_status = "Pass" if percentage >= 60 else "Fail"
                st.write(f"{subject}: {score}/10 ({percentage:.1f}%) - {pass_fail_status}")
                total_score += score 

                # Count correct/incorrect answers
                if percentage >= 60:
                    num_correct += 1
                else:
                    num_incorrect += 1

        # Calculate the percentage of total score
        max_possible_score = 10 * len(st.session_state.scores)
        total_percentage = (total_score / max_possible_score) * 100
        st.write(f"**Total Score:** {total_score}/{max_possible_score} ({total_percentage:.1f}%)")

    with col2:
        correct_score = total_score
        incorrect_score = max_possible_score - total_score

        # Donut chart
        fig, ax = plt.subplots(figsize=(6, 6))  
        wedges, texts, autotexts = ax.pie(
            [correct_score, incorrect_score],
            labels=["Correct", "Incorrect"],
            autopct='%1.1f%%',
            startangle=140,
            pctdistance=0.85,  
            colors=['lightgreen', 'lightgrey'],
            wedgeprops=dict(width=0.3, edgecolor='none') 
        )

        # Set the background of the plot to transparent
        ax.set_facecolor('none')

        # Draw a circle at the center to make it a donut chart (transparent center)
        center_circle = plt.Circle((0, 0), 0.70, color='white', fc='white', edgecolor='white')
        ax.add_artist(center_circle)

        # Display the donut chart in Streamlit
        st.pyplot(fig)

    scores = list(st.session_state.scores.values())
    subjects = list(st.session_state.scores.keys())
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = ['skyblue', 'pink', 'red', 'green', 'lightgreen']

    # Create bars and annotate the scores
    bars = ax.bar(subjects, scores, color=colors[:len(subjects)])
    ax.set_title("Score per Subject (Bar Graph)")
    ax.set_xlabel("Subjects")
    ax.set_ylabel("Scores")

    # Add scores on top of each bar
    for bar in bars:
        yval = bar.get_height()
        ax.annotate(f'{yval}', xy=(bar.get_x() + bar.get_width() / 2, yval), 
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom')

    # Display bar graph
    st.pyplot(fig)

    # Check if user passed or failed
    if len(failed_subjects) >= 2:
        st.write("""If you'd like to try again, click below to retake the test and show us how much you've improved!""", unsafe_allow_html=True)

        if st.button("Retake Test"):
            # Reset all session state variables
            st.session_state.scores = {key: None for key in st.session_state.scores.keys()}
            st.session_state.answered_subjects = set()
            st.session_state.current_subject = None
            st.session_state.current_questions = []
            st.rerun()
        
        st.subheader("or")
        if st.button("Go back to home"):
            st.session_state.scores = {key: None for key in st.session_state.scores.keys()}
            st.session_state.answered_subjects = set()
            st.session_state.current_subject = None
            st.session_state.current_questions = []
            st.session_state['page'] = 'home'
            st.rerun()
        
        st.write("""Don't worry! Everyone faces challenges, and failure is just part of the learning process. Use this as an opportunity to focus on areas that need improvement.""", unsafe_allow_html=True)
        st.image('https://i.pinimg.com/originals/e7/fb/06/e7fb06e185abb65900e4344a3d715751.png', width=700)
    else:
        st.success("Congratulations! You passed the test.")
        # Save results to result.py
        with open("result.py", "w") as f:
            f.write(f"results = {st.session_state.scores}")
        st.write("Results saved to result.py")

def test():
    if all(subject in st.session_state.answered_subjects for subject in st.session_state.scores.keys()):
        final_results()
    elif st.session_state.current_subject:
        display_questions(st.session_state.current_subject)
    else:
        display_selection()
