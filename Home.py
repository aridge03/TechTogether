import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain


def main():


    rain(
        emoji="👩🏾‍🔬,👨🏽‍💼",
        font_size=25,
        falling_speed=10,
        animation_length="infinite", 

    )



    # Title with increased font size and bold styling
    st.markdown(
    "<h1 style='text-align: center; color: white; font-size: 3em; font-weight: bold;'>Welcome to</h1>",
    unsafe_allow_html=True
    )
  

    # Title with increased font size and bold styling
    st.markdown(
    "<h2 style='text-align: center; color: white; font-size: 3em;'>" \
    "🌺Quizzing the Wage Divide:🌺<br>A Gender Gap Guessing Game</h2>",
    unsafe_allow_html=True
    )
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown(
    "<div style='font-size: 1.5em; text-align: center;'>"
    "This interactive experience is designed to help gauge your understanding of the challenges that marginalized genders face in the workplace. "
    "To begin this enlightening journey, press the button below and tackle the 20 thought-provoking questions that await you. "
    "Let's strive for a more equitable future together!"
    "</div>",
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
