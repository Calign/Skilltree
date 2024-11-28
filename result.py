import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the data for bachelor degree
bachelor_data = pd.read_excel("bachelor_degree.xlsx")

def calculate_percentage(score, total):
    """Calculate the percentage of the user's score."""
    return round((score / total) * 100, 2)

def get_recommendations(scores, data, num_recommendations=5):
    """Recommend bachelor courses based on the user's test scores."""
    # Calculate the difference of total score for each degree
    data["Score_Difference"] = data[["English", "Math", "History", "Science", "Filipino"]].apply(
        lambda row: sum(abs(row[col] - scores[col]) for col in scores.keys()),
        axis=1
    )
    # Sort degrees by the smallest score difference
    recommended_degrees = data.sort_values("Score_Difference").head(num_recommendations)
    return recommended_degrees

def result():
    st.title("Bachelor Degree Aptitude Test Results")

    # Make sure that scores exist in session state
    if "scores" in st.session_state and any(st.session_state.scores.values()):
        scores = st.session_state.scores
        percentages = {subject: calculate_percentage(score, 10) for subject, score in scores.items() if score is not None}

        # Display the score of the user
        st.subheader("Your Scores")
        st.markdown("<hr style='border: 1px solid black;' />", unsafe_allow_html=True)
        for subject, score in scores.items():
            if score is not None:
                percentage = percentages[subject]
                st.write(f"**{subject}:** {score}/10 ({percentage}%)")

        # Horizontal Bar Chart with subjects on x-axis and numerical scale on y-axis
        fig, ax = plt.subplots(figsize=(8, 6))  # Set a larger size for clarity
        ax.bar(list(scores.keys()), list(scores.values()), color=['skyblue', 'pink', 'red', 'green', 'lightgreen'])
        ax.set_title("Your Scores by Subject")
        ax.set_ylabel("Scores")
        ax.set_xlabel("Subjects")
        ax.set_ylim(0, 10)
        st.pyplot(fig)

        st.markdown("<hr style='border: 1px solid black;' />", unsafe_allow_html=True)

        # Recommend degrees based on the user's scores
        st.subheader("Top 5 Recommended Bachelor Degree Programs")
        recommendations = get_recommendations(scores, bachelor_data)
        for _, row in recommendations.iterrows():
            st.markdown(f"### {row['Degree_program']}")
            st.write(f"**Description:** {row['Description']}")
            st.write(f"**Career Paths:** {row['Career']}")
            st.write("---")
        st.subheader("Congratulations on Passing the Test!")

        st.markdown("<hr style='border: 1px solid black;' />", unsafe_allow_html=True)

        # Button to return to home
        if st.button("Go Home"):
            st.session_state.scores = {key: None for key in st.session_state.scores.keys()}
            st.session_state.answered_subjects = set()
            st.session_state.current_subject = None
            st.session_state.current_questions = []
            st.session_state["page"] = "home"
            st.rerun()
    else:
        st.warning("No scores available. Please complete the test or use the 'Test run skip' feature.")
        if st.button("Go Home"):
            st.session_state["page"] = "home"
            st.rerun()
