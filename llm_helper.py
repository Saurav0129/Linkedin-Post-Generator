from langchain_groq import ChatGroq
import os
import streamlit as st

groq_api = st.secrets["api_keys"]["GROQ_API_KEY"]

llm = ChatGroq(
    groq_api_key=groq_api, 
    model_name="gemma2-9b-it",
    temperature=0.2
)

if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)