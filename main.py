import openai
import streamlit as st

openai.api_key = st.secrets["openai_api_key"]

st.title("Chatbot using Davinci")


def fine_tune_model(question, answer):
    prompt = (question, answer)

    model_engine = "text-davinci-002"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return model_engine


def generate_response(prompt, model_engine):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message


question = st.text_input("Enter a question")
answer = st.text_area("Enter an answer")

if st.button("Fine-tune model"):
    model_engine = fine_tune_model(question, answer)
    st.success("Model fine-tuned!")

if st.button("Generate response"):
    response = generate_response(question, model_engine)
    st.success(response)


# prompt = st.text_input("Enter your message:")
#
# if prompt:
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         max_tokens=1024
#     )
#     st.write("Bot:", response["choices"][0]["text"])
#
#
# st.title("Chatbot using Davinci-002")
#
# prompt = st.text_input("Enter your message:")
#
# if prompt:
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=prompt,
#         max_tokens=1024
#     )
#     st.write("Bot:", response["choices"][0]["text"])
