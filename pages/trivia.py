import streamlit as st

def show_trivia_page():
    st.title("Trivia")
    options = ["$0.80", "$1.50", "$2.50", "$3.00"]
    correct_option = "$3.00"  # The correct answer
    selected_option = st.radio("How much less per hour do girls aged 12 to 18 experience receive during a summer job?",options)

    # Check if the selected option is correct
    if selected_option == correct_option:
        st.success("Correct!")
    else:
        st.error("Incorrect.")
