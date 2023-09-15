import streamlit as st
from pages.trivia import show_trivia_page
from pages.timeline import show_timeline_page

def main():
    st.sidebar.title("Navigation")
    selected_page = st.sidebar.radio("Go to", ("Trivia", "Timeline"))

    if selected_page == "Trivia":
        show_trivia_page()
    elif selected_page == "Timeline":
        show_timeline_page()

if __name__ == "__main__":
    main()