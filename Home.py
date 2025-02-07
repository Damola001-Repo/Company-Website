import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.title('The Best Company')
st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
st.subheader('Our Team')
col1, col2, col3 = st.columns(3)

data = pd.read_csv('data.csv')
topics = pd.read_csv('topics.csv')

with col1:
    for index, row in data[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images/'+row['image'])

with col2:
    for index, row in data[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images/'+row['image'])

with col3:
    for index, row in data[8:12].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images/'+row['image'])