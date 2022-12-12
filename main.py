import openai
import streamlit as st

openai.api_key = st.secrets["openai_api_key"]

st.title("Chatbot Example")

prompt = st.text_input("Enter your message:")

if prompt:
    response = openai.Completion.create(
        # engine="text-davinci-002",
        engine="davinci",
        prompt=prompt,
        max_tokens=1024
    )
    st.write("Bot:", response["choices"][0]["text"])