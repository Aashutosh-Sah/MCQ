import streamlit as st
import sqlite3
from quiz_game import get_random_questions, save_score, get_leaderboard, add_question


# Streamlit App Title

st.set_page_config(page_title="Quiz Game", page_icon="📚")
st.title("Quiz Game")

# Sidebar Menu
menu = ["Home", "Admin Panel", "Game Mode", "User Manual"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.header("Welcome to the Quiz Game!")
    st.write("""
    This is a quiz game where you can test your knowledge by answering multiple-choice questions.
    You can choose between 10, 50, or 100 questions in Game Mode.
    After completing the quiz, your score will be saved in the database.
    """)

elif choice == "Admin Panel":
    st.header("Admin Panel")
    admin_id = st.text_input("Admin ID")
    admin_password = st.text_input("Password", type="password")

    if admin_id == "admin01" and admin_password == "admin_ofc":
        st.success("Logged in as Admin")
        st.subheader("Add a New Question")
        question = st.text_area("Question")
        option1 = st.text_input("Option 1")
        option2 = st.text_input("Option 2")
        option3 = st.text_input("Option 3")
        option4 = st.text_input("Option 4")
        correct_option = st.selectbox("Correct Option", [option1, option2, option3, option4])

        if st.button("Submit Question"):
            add_question(question, option1, option2, option3, option4, correct_option)
            st.success("Question added successfully!")
    else:
        st.error("Invalid Admin ID or Password")

elif choice == "Game Mode":
    st.header("Game Mode")
    num_questions = st.selectbox("Select Number of Questions", [10, 50, 100])
    start_quiz = st.button("Start Quiz")

    if start_quiz:
        questions = get_random_questions(num_questions)
        st.session_state['questions'] = questions
        st.session_state['score'] = 0
        st.session_state['current_question'] = 0

    if 'questions' in st.session_state:
        current_question_index = st.session_state['current_question']
        if current_question_index < len(st.session_state['questions']):
            question_data = st.session_state['questions'][current_question_index]
            question_id, question, option1, option2, option3, option4, correct_option = question_data

            st.subheader(f"Question {current_question_index + 1}")
            st.write(question)
            selected_option = st.radio("Options", [option1, option2, option3, option4])
            
            # Submit Button
            if st.button("Submit"):
                if selected_option:
                    # Check answer
                    if selected_option == correct_option:
                        st.session_state['score'] += 1  # Increment score if correct
                    st.session_state['current_question'] += 1  # Move to next question
                    st.rerun()  # Refresh page to load next question
                else:
                    st.warning("Please select an answer before submitting.")

        else:
            st.success("Quiz Completed!")
            name = st.text_input("Enter your name to save your score:")
            if st.button("Save Score"):
                save_score(name, st.session_state['score'], num_questions)
                st.success(f"Score saved! Your score: {st.session_state['score']} / {num_questions}")

                # Show Leaderboard
                leaderboard = get_leaderboard(num_questions)
                st.subheader("Leaderboard")
                for rank, (player_name, player_score) in enumerate(leaderboard, 1):
                    st.write(f"{rank}. {player_name}: {player_score}")


elif choice == "User Manual":
    st.header("User Manual")
    st.write("""
    - **Home**: Displays an overview of the quiz game.
    - **Admin Panel**: Allows admins to add new questions to the database.
      - Login with ID: `admin01` and Password: `admin_ofc`.
    - **Game Mode**: Start a quiz by selecting the number of questions (10, 50, or 100).
      - After completing the quiz, enter your name to save your score.
      - View the leaderboard based on the number of questions played.
    - **User Manual**: Provides instructions on how to use the app.
    """)
