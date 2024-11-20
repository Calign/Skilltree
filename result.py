import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt

# Load the dataset from Excel
df = pd.read_excel('bachelor_degree.xlsx')

# Normalize the degree programs' subject scores
scaler = MinMaxScaler()
df[['English', 'Math', 'History', 'Science', 'Filipino']] = scaler.fit_transform(df[['English', 'Math', 'History', 'Science', 'Filipino']])

def result():
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background: #ffffff;
    background-size: cover;
    }

    [data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0)
    }
    """ 
    st.markdown(page_bg_img, unsafe_allow_html=True)


    st.title("Test Results")
    
    # Retrieve scores from session state (user's scores)
    subject_scores = st.session_state.get('subject_scores', {})
    
    if subject_scores:
        st.write("### Your Scores by Subject")
        
        # Create a bar chart of the user's scores
        subject_names = list(subject_scores.keys())
        scores = list(subject_scores.values())
        
        # Create the bar chart
        fig, ax = plt.subplots()
        ax.bar(subject_names, scores, color='skyblue')
        ax.set_xlabel("Subjects")
        ax.set_ylabel("Scores")
        ax.set_title("Your Scores by Subject")
        st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)
        
        # Show the bar chart in Streamlit
        st.pyplot(fig)

        st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)

        # Normalize the user's scores
        user_preferences = {subject: score for subject, score in subject_scores.items()}
        
        # Normalize the user's scores (same as the degree programs)
        user_df = pd.DataFrame([user_preferences])
        user_df[['English', 'Math', 'History', 'Science', 'Filipino']] = scaler.transform(user_df[['English', 'Math', 'History', 'Science', 'Filipino']])

        # Initialize KNN model
        knn = NearestNeighbors(n_neighbors=5, metric='euclidean')  # n_neighbors is the number of closest programs to recommend
        
        # Fit the model on the degree programs' scores
        knn.fit(df[['English', 'Math', 'History', 'Science', 'Filipino']])

        # Find the nearest neighbors (degree programs) to the user's scores
        distances, indices = knn.kneighbors(user_df[['English', 'Math', 'History', 'Science', 'Filipino']])

        # Display top 5 recommended programs with degree program, description, and career
        st.write("### Top 5 Recommended Degree Programs")
        for i in range(5):
            degree_program = df.iloc[indices[0][i]]['Degree_program']
            description = df.iloc[indices[0][i]]['Description']
            career = df.iloc[indices[0][i]]['Career']

            st.write(f"**Degree Program:** {degree_program}")
            st.write(f"**Description:** {description}")
            st.write(f"**Career:** {career}")
            st.write("---")  # Adding a separator between each result

    else:
        st.write("No scores available. Please complete the test first.")
    
    # Option to go back to the main or home page if needed
    if st.button("Back to Home"):
        st.session_state['page'] = 'home'
        st.rerun()
