from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


langchain_api_key = os.getenv("LANGCHAIN_API_KEY")


if not langchain_api_key:
    raise ValueError("LANGCHAIN_API_KEY environment variable is not set")


os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = langchain_api_key


prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question:{question}")
    ]
)

#streamlit framwework

st.title("LangChain Llama3 chatbot")
input_text= st.text_input("Search the topic you want")

#open ai LLm

llm= Ollama(model="llama3")
output_parser=StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
