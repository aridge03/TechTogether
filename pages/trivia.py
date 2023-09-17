import streamlit as st

def show_trivia_page():
    centered_title = '<h1 style="text-align:center;">Gender Pay Gap Quiz</h1>'
    st.markdown(centered_title, unsafe_allow_html=True)
    session_state = st.session_state

    if 'current_question' not in session_state:
        session_state.current_question = 0

    if 'score' not in session_state:
        session_state.score = 0

    if 'user_answers' not in session_state:
        session_state.user_answers = []

    questions = [
        {
            'question': 'Which of the following is a common factor contributing to the gender pay gap? ',
            'options': ["Women's stronger negotiation skills", 'Occupational segregation', 'Equal representation in leadership roles', 'Lack of educational opportunities for women'],
            'correct_answer': 'Occupational segregation',
            'source': ""
        },
        {
            'question': 'What is the approximate gender pay gap per hour experienced by girls aged 12 to 18 in summer jobs?',
            'options': ['$0.00', '$1.00', '$3.00', '$8.00'],
            'correct_answer': '$3.00',
            'source': "https://canadianwomen.org/the-facts/the-gender-pay-gap/"
        },
        {
            'question': 'What is the gender pay gap typically measured as?',
            'options': ['Difference in working hours', 'Difference in earnings between men and women', 'Difference in job satisfaction', 'Difference in educational attainment Correct'],
            'correct_answer': 'Difference in earnings between men and women',
            'source': ""
        },
        {
            'question': 'What percentage of a pension do women typically retire with compared to men? ',
            'options': ['80%', '70%', '60%', '50%'],
            'correct_answer': '80%',
            'source': "https://canadianwomen.org/the-facts/the-gender-pay-gap/"
        },
        {
            'question': 'In the global ranking of gender gap in overall economic participation and opportunity, where does Canada stand out of 156 countries? ',
            'options': ['10th', '20th', '30th', '40th'],
            'correct_answer': '40th',
            'source': "https://canadianwomen.org/the-facts/the-gender-pay-gap/"
        },
        {
            'question': 'In 2016, for every dollar earned by men in Canada, how much did women working full-time typically earn? ',
            'options': ['75 cents', '80 cents', '85 cents', '90 cents'],
            'correct_answer': '75 cents',
            'source': "https://canadianwomen.org/wp-content/uploads/2018/08/Gender-Wage-Gap-Fact-Sheet_AUGUST-2018_FINAL1.pdf"
        },
        {
            'question': 'According to data from the 2016 Census: Indigenous women working full-time, full-year earn approximately what percent less than non-Indigenous men? ',
            'options': ['5%', '15%', '35%', '50%'],
            'correct_answer': '35%',
            'source': "https://canadianwomen.org/wp-content/uploads/2018/08/Gender-Wage-Gap-Fact-Sheet_AUGUST-2018_FINAL1.pdf"
        },
        {
            'question': 'According to data from the 2016 Census: Racialized women working full-time, full year earn approximately what percent less than nonracialized men? ',
            'options': ['3%', '13%', '23%', '33%'],
            'correct_answer': '33%',
            'source': "https://canadianwomen.org/wp-content/uploads/2018/08/Gender-Wage-Gap-Fact-Sheet_AUGUST-2018_FINAL1.pdf"
        },
        {
            'question': 'What is the "Motherhood Penalty" referring to in the context of the gender pay gap? ',
            'options': ['A penalty for women who choose not to have children', 'A penalty for women who work part-time', 'A penalty for women with children, who often experience lower wages', 'A penalty for women who prioritize their careers over family'],
            'correct_answer': 'A penalty for women with children, who often experience lower wages',
            'source': ""
        },
        {
            'question': 'According to a 2017 study by the World Economic Forum, approximately how many more years, at present trends, would it take to close the economic gender gap worldwide?',
            'options': ['11 years', '59 years', '184 years', '268 years'],
            'correct_answer': '268 years',
            'source': "https://canadianwomen.org/the-facts/the-gender-pay-gap/"
        },
        {
            'question': 'Even with similar or higher education levels, transgender individuals, on average, face a wage gap compared to cisgender individuals. How much higher are the wages for cisgender individuals?',
            'options': ['22%', '32%', '42%', '52%'],
            'correct_answer': '32%',
            'source': "https://www.forbes.com/sites/jamiewareham/2021/11/17/transgender-pay-gap-revealed-cisgender-people-paid-32-more/?sh=23c635a717b2"
        },
        {
            'question': 'The gender pay gap tends to be wider for women who:',
            'options': ['Work in male-dominated fields', 'Have higher levels of education', 'Live in urban areas', 'Have more years of work experience'],
            'correct_answer': 'Work in male-dominated fields',
            'source': ""
        },
        {
            'question': 'In 2018, transgender employees were how many times more likely to experience unwanted behaviors in the workplace compared to cisgender employees, including inappropriate sexual jokes, unwanted sexual and physical attention, and suggestions regarding their behavior? ',
            'options': ['1.5 times', '2 times', '2.5 times', '3 times'],
            'correct_answer': '3 times',
            'source': "https://www.payequitychrc.ca/sites/payequity/files/2022-02/Promising%20practices%20-%20Collecting%20inclusive%20gender%20data.pdf"
        },
        {
            'question': 'When is International Equal Pay Day celebrated? ',
            'options': ['September 18th', 'March 8th', 'December 13th', 'January 1st'],
            'correct_answer': 'September 18th',
            'source': "https://nationaltoday.com/international-equal-pay-day/"
        },
        {
            'question': "What is the term used to describe the cumulative impact of the gender pay gap over a woman's career?",
            'options': ['Career gap', 'Income disparity', 'Wage discrimination', 'Lifetime earnings gap'],
            'correct_answer': 'Lifetime earnings gap',
            'source': ""
        },
        {
            'question': "In the 1980s, women, on average, were making approximately how much of what men in the same jobs were earning?",
            'options': ['62%', '78%', '84%', '99%'],
            'correct_answer': '62%',
            'source': "https://www.womenonbusiness.com/countdown-to-equal-pay-day-the-gender-pay-gap-in-the-1980s/#:~:text=Rather%20than%20earning%20only%2060%25%20of%20what%20a,a%20woman%20in%20the%201970s%20would%20have%20earned."
        },
        {
            'question': "What percentage of chief executive roles in the US are occupied by women?",
            'options': ['12.2%', '29.2%', '45.2%', '53.2%'],
            'correct_answer': '29.2%',
            'source': "https://moneyzine.com/careers-resources/female-ceo-statistics/"
        },
        {
            'question': "In 2020, women in top executive positions earned approximately what percentage less than their male counterparts?",
            'options': ['50%', '60%', '70%', '75%'],
            'correct_answer': '75%',
            'source': "https://moneyzine.com/careers-resources/female-ceo-statistics/"
        },
        {
            'question': "In October 2022, what percentage of newly appointed CEOs were women or non-binary? ",
            'options': ['19.4%', '26.1%', '40.3%', '64.8%'],
            'correct_answer': '26.1%',
            'source': "https://moneyzine.com/careers-resources/female-ceo-statistics/"
        },
        {
            'question': "Women are what percentage less likely than men to get promoted out of an entry-level job ",
            'options': ['10%', '20%', '30%', '40%'],
            'correct_answer': '30%',
            'source': "https://canadianwomen.org/the-facts/women-and-leadership-in-canada/"
        },
    ]
    outcomes = [
        {
            'level':'Limited Understanding',
            'feedback':'Your knowledge about the gender pay gap is limited. Consider reviewing the basics of gender pay disparities to enhance your understanding.'
        },
        {
            'level':'Basic Awareness',
            'feedback':'You have a foundational understanding of the gender pay gap. Keep learning and exploring more in-depth information to improve your awareness.'
        },
        {
            'level':'Moderate Understanding',
            'feedback':'You possess a moderate understanding of the gender pay gap. Keep studying to gain a deeper understanding of its complexities and implications.'
        },
        {
            'level':'Good Knowledge',
            'feedback':'"Your knowledge of the gender pay gap is good. Continue to explore various aspects and stay informed about the latest research and developments in this area.'
        },
        {
            'level':'Excellent Understanding',
            'feedback':'Congratulations! You have an excellent understanding of the gender pay gap. Stay engaged with ongoing discussions and efforts to address this issue for a more equitable future.'
        }


    ]


    if session_state.current_question < len(questions):
        question_data = questions[session_state.current_question]
        st.write(f'#### **Question {session_state.current_question + 1}:** {question_data["question"]}')
        selected_option = st.radio('Select an option:', question_data['options'])
        col1, col2 = st.columns(2)
        if (session_state.current_question == len(questions)-1 and col2.button('Finish')) or (session_state.current_question < len(questions)-1 and col2.button('Next Question')):
            if selected_option == question_data['correct_answer']:
                session_state.score += 1
            session_state.user_answers.append(selected_option)
            session_state.current_question += 1
            st.experimental_rerun()
        if session_state.current_question !=0 and col1.button('Previous Question'):
            session_state.current_question -= 1
            st.experimental_rerun()
    else:
        centered_message = '<p style="text-align:center;">Quiz completed. Thanks for playing! Your score is: {}/20</p>'.format(session_state.score)
        st.markdown(centered_message, unsafe_allow_html=True)
        if session_state.score<=4:
            result = outcomes[0]
        elif session_state.score<=8:
            result = outcomes[1]
        elif session_state.score<=12:
            result = outcomes[2]
        elif session_state.score<=16:
            result = outcomes[3]
        else:
            result = outcomes[4]
        st.write('')
        centered_text = '<div style="text-align:center; font-size:24px;">Basic Awareness</div>'
        st.markdown(centered_text, unsafe_allow_html=True)
        st.write('')
        st.write(result['feedback'])

        st.write('')
        with st.expander('Summary of Your Answers:'):
            for i, question_data in enumerate(questions):
                st.write(f'Question {i + 1}: {question_data["question"]}')
                st.write(f'Your Answer: {session_state.user_answers[i] if "user_answers" in session_state else "Not answered"}')
                st.write(f'Correct Answer: {question_data["correct_answer"]}')
                st.write(f'Source: {question_data["source"]}')
                st.write('')
                st.write('')
def main():
    show_trivia_page()
if __name__ == "__main__":
    main()
