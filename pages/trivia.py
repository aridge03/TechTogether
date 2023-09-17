import streamlit as st

def show_trivia_page():
    st.title('Gender Pay Gap Quiz')
    session_state = st.session_state

    if 'current_question' not in session_state:
        session_state.current_question = 0

    if 'score' not in session_state:
        session_state.score = 0

    questions = [
        {
            'question': 'Which of the following is a common factor contributing to the gender pay gap? ',
            'options': ["Women's stronger negotiation skills", 'Occupational segregation', 'Equal representation in leadership roles', 'Lack of educational opportunities for women'],
            'correct_answer': 'Occupational segregation'
        },
        {
            'question': 'What is the approximate gender pay gap per hour experienced by girls aged 12 to 18 in summer jobs?',
            'options': ['$0.00', '$1.00', '$3.00', '$8.00'],
            'correct_answer': '$3.00'
        },
        {
            'question': 'What is the gender pay gap typically measured as?',
            'options': ['Difference in working hours', 'Difference in earnings between men and women', 'Difference in job satisfaction', 'Difference in educational attainment Correct'],
            'correct_answer': 'Difference in earnings between men and women'
        },
        {
            'question': 'What percentage of a pension do women typically retire with compared to men? ',
            'options': ['80%', '70%', '60%', '50%'],
            'correct_answer': '80%'
        },
        {
            'question': 'In the global ranking of gender gap in overall economic participation and opportunity, where does Canada stand out of 156 countries? ',
            'options': ['10th', '20th', '30th', '40th'],
            'correct_answer': '40th'
        },
        {
            'question': 'In 2016, for every dollar earned by men in Canada, how much did women working full-time typically earn? ',
            'options': ['75 cents', '80 cents', '85 cents', '90 cents'],
            'correct_answer': '75 cents'
        },
        {
            'question': 'According to data from the 2016 Census: Indigenous women working full-time, full-year earn approximately what percent less than non-Indigenous men? ',
            'options': ['5%', '15%', '35%', '50%'],
            'correct_answer': '35%'
        },
        {
            'question': 'According to data from the 2016 Census: Racialized women working full-time, full year earn approximately what percent less than nonracialized men? ',
            'options': ['3%', '13%', '23%', '33%'],
            'correct_answer': '33%'
        },
        {
            'question': 'What is the "Motherhood Penalty" referring to in the context of the gender pay gap? ',
            'options': ['A penalty for women who choose not to have children', 'A penalty for women who work part-time', 'A penalty for women with children, who often experience lower wages', 'A penalty for women who prioritize their careers over family'],
            'correct_answer': 'A penalty for women with children, who often experience lower wages'
        },
        {
            'question': 'According to a 2017 study by the World Economic Forum, approximately how many more years, at present trends, would it take to close the economic gender gap worldwide?',
            'options': ['11 years', '59 years', '184 years', '268 years'],
            'correct_answer': '268 years'
        },
        {
            'question': 'Even with similar or higher education levels, transgender individuals, on average, face a wage gap compared to cisgender individuals. How much higher are the wages for cisgender individuals?',
            'options': ['22%', '32%', '42%', '52%'],
            'correct_answer': '32%'
        },
        {
            'question': 'The gender pay gap tends to be wider for women who:',
            'options': ['Work in male-dominated fields', 'Have higher levels of education', 'Live in urban areas', 'Have more years of work experience'],
            'correct_answer': 'Work in male-dominated fields'
        },
        {
            'question': 'In 2018, transgender employees were how many times more likely to experience unwanted behaviors in the workplace compared to cisgender employees, including inappropriate sexual jokes, unwanted sexual and physical attention, and suggestions regarding their behavior? ',
            'options': ['1.5 times', '2 times', '2.5 times', '3 times'],
            'correct_answer': '3 times'
        },
        {
            'question': 'When is International Equal Pay Day celebrated? ',
            'options': ['September 18th', 'March 8th', 'December 13th', 'January 1st'],
            'correct_answer': 'September 18th'
        },
        {
            'question': "What is the term used to describe the cumulative impact of the gender pay gap over a woman's career?",
            'options': ['Career gap', 'Income disparity', 'Wage discrimination', 'Lifetime earnings gap'],
            'correct_answer': 'Lifetime earnings gap'
        },
        {
            'question': "In the 1980s, women, on average, were making approximately how much of what men in the same jobs were earning?",
            'options': ['62%', '78%', '84%', '99%'],
            'correct_answer': '62%'
        },
        {
            'question': "What percentage of chief executive roles in the US are occupied by women?",
            'options': ['12.2%', '29.2%', '45.2%', '53.2%'],
            'correct_answer': '29.2%'
        },
        {
            'question': "In 2020, women in top executive positions earned approximately what percentage less than their male counterparts?",
            'options': ['50%', '60%', '70%', '75%'],
            'correct_answer': '75%'
        },
        {
            'question': "In October 2022, what percentage of newly appointed CEOs were women or non-binary? ",
            'options': ['19.4%', '26.1%', '40.3%', '64.8%'],
            'correct_answer': '26.1%'
        },
        {
            'question': "Women are what percentage less likely than men to get promoted out of an entry-level job ",
            'options': ['10%', '20%', '30%', '40%'],
            'correct_answer': '30%'
        },
    ]

    if session_state.current_question < len(questions):
        question_data = questions[session_state.current_question]
        st.write(f'**Question {session_state.current_question + 1}:** {question_data["question"]}')
        selected_option = st.radio('Select an option:', question_data['options'])
        col1, col2 = st.columns(2)
        if col2.button('Next Question'):
            if selected_option == question_data['correct_answer']:
                session_state.score += 1
            st.write('Moving to the next question...')
            session_state.current_question += 1
            st.experimental_rerun()
        if session_state.current_question !=0 and col1.button('Previous Question'):
            session_state.current_question -= 1
            st.experimental_rerun()
    else:
        st.write('Quiz completed. Thanks for playing! Your score is', str(session_state.score) + "/" + str(len(questions)))