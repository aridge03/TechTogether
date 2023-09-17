import streamlit as st
from pages.trivia import show_trivia_page

def main():
    # Title with increased font size and bold styling
    st.markdown(
    "<h1 style='text-align: center; color: white; font-size: 3em; font-weight: bold; " \
    "text-shadow: -2px -2px 0 #8a2be2, 2px -2px 0 #8a2be2, -2px 2px 0 #8a2be2, 2px 2px 0 #8a2be2;'>Welcome to</h1>",
    unsafe_allow_html=True
    )

    # Title with increased font size and bold styling
    st.markdown(
    "<h2 style='text-align: center; color: white; font-size: 6em; " \
    "text-shadow: -2px -2px 0 #8a2be2, 2px -2px 0 #8a2be2, -2px 2px 0 #8a2be2, 2px 2px 0 #8a2be2;'>" \
    "Quizzing the Wage Divide: A Gender Gap Guessing Game</h2>",
    unsafe_allow_html=True
    )
    if st.button("Start Trivia"):
        show_trivia_page()

if __name__ == "__main__":
    main()