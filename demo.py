from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash-exp")


def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


st.header("Gemini LLM Application")
st.subheader("Build with Gemini")


input = st.text_input("Input your Prompt")
submit = st.button("Ask")

if submit and input:
    response = get_gemini_response(input)
    st.write(response)



