import streamlit as st
from functions.send_email import send_email
import pandas as pd

df = pd.read_csv('topics.csv')

st.title('Contact Us')
form = st.form(key='form')

with form:
    email = st.text_input(label='Your Email Address')
    topic = st.selectbox(
        "What topic do you want to discuss?",
        df['topic']
    )
    raw_message = st.text_area(label='Text')
    button = st.form_submit_button(label='Send Mail')
    message = f"""\
Subject: New email from {email}

From: {email}
Topic: {topic}
{raw_message}
"""

    if button:
        send_email(message)