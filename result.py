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

    # Ensure scores exist in session state
    if "scores" in st.session_state and any(st.session_state.scores.values()):
        scores = st.session_state.scores
        total_possible_score = len(scores) * 10  # Each subject is out of 10 points
        total_score = sum(score for score in scores.values() if score is not None)
        overall_percentage = calculate_percentage(total_score, total_possible_score)
        st.subheader("Your Scores")
        st.markdown("<hr style='border: 1px solid black;' />", unsafe_allow_html=True)
        col1, col2 = st.columns(2)

        with col1:
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.write(" ")
            for subject, score in scores.items():
                if score is not None:
                    percentage = calculate_percentage(score, 10)
                    st.write(f"**{subject}:** {score}/10 ({percentage}%)")

            # Display overall score in text
            st.write(f"**Total Score:** {total_score}/{total_possible_score} ({overall_percentage}%)")
        with col2:
        # Donut chart for overall percentage
            fig, ax = plt.subplots(figsize=(3, 3))  # Adjusted size for a smaller chart
            fig.patch.set_facecolor('none')  # Remove the white background

            # Data for the chart
            sizes = [overall_percentage, 100 - overall_percentage]
            colors = ['#4CAF50', '#E0E0E0']
            labels = ['Correct', 'Incorrect']

            # Plot the donut chart
            wedges, texts, autotexts = ax.pie(
                sizes,
                labels=labels,
                autopct='%1.1f%%',
                startangle=90,
                colors=colors,
                wedgeprops={'width': 0.3, 'edgecolor': 'white'},
                textprops={'fontsize': 10}
            )

            # Make it a donut by adding a circle at the center
            center_circle = plt.Circle((0, 0), 0.7, color='white', fc='white')
            ax.add_artist(center_circle)

            # Display the chart in Streamlit
            st.pyplot(fig)


        # Horizontal bar chart with subjects and scores
        st.subheader("Your Scores by Subject")
        fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the figure size as needed
        bars = ax.bar(list(scores.keys()), list(scores.values()), color=['skyblue', 'pink', 'red', 'green', 'lightgreen'])
        ax.set_title("Your Scores by Subject")
        ax.set_ylabel("Scores")
        ax.set_xlabel("Subjects")
        ax.set_ylim(0, 10)

        # Add labels inside the bars
        ax.bar_label(bars, fmt='%d', padding=3, color='black') 

        # Display the chart in Streamlit
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
