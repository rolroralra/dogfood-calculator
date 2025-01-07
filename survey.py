import streamlit as st
import re


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # Simple regex for email validation
    return re.match(pattern, email) is not None


def display_textbox(header="Question Title", textbox_title="Input here: "):
    st.subheader(header)
    return st.text_area(textbox_title)


def display_radio(header="Question Title", radio_title="", index=None, options=["Yes", "No"]):
    st.subheader(header)
    return st.radio(radio_title, index=index, options=options)


def display_checkbox(header="Qustion Title", options=[1, 2, 3], other_option=None, other_option_comment=""):
    st.subheader(header)
    
    response = []
    for option in options:
        if st.checkbox(option):
            response.append(option)

    if other_option:
        if st.checkbox(other_option):
            response.append(st.text_input(other_option_comment))

    return response


if __name__ == "__main__":
    st.title("Education Survey")

    email = st.text_input("Please enter your email address:")

    if email:
        if not is_valid_email(email):
            st.error("Please enter a valid email address.")
        else:
            responses = {}
            
            responses['q1'] = display_radio(header="Please evaluate your overall satisfaction with Education", 
                                            radio_title="Select only one choice.",
                                            index=None,
                                            options=["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"]) 

            responses['q2'] = display_checkbox(header="Please select your interesting part.",
                                               options=["Java", "Kotlin", "Typescript", "Nextjs", "Rust", "Python", "Nodejs"],
                                               other_option="Other (Please Specify)", other_option_comment="Please specify")

            responses['q3'] = display_textbox(header="If there is any conference you would like to receive, please feel free to share.",
                                              textbox_title="Your suggestion: ")

            if st.button("제출"):
                st.write(responses)
                st.write("감사합니다! 귀하의 응답이 제출되었습니다.")
    else:
        st.info("Please enter your email address to participate in the survey.")
