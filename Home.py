import streamlit as st
from streamlit_extras.switch_page_button import switch_page


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
    col1, col2,col3= st.columns(3)
    with col1:
        st.write("")
        
    with col2:
        if st.button("Click Here To Start The Trivia!"):
            switch_page("Trivia")
    

if __name__ == "__main__":
    main()