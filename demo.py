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


st.header("Gemini LLM Application for your any queries")
st.subheader("Build with Gemini 2.0 see its capabilities")


input = st.text_input("Input your Prompt")
submit = st.button("Ask")

if submit and input:
    response = get_gemini_response(input)
    st.write(response)



