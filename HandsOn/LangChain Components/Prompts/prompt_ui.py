from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate

import os
import streamlit as st

load_dotenv()

api_key=os.getenv("GROQ_API_KEY","").strip()

model=ChatGroq(
    model="qwen/qwen3.8-27b",
    api_key=api_key,
    temperature=0.2,
    max_tokens=512,
)

st.header("LangChain Google Gemini Chat Example")   

paper_input=st.selectbox("Select a paper", ["GPT-3", "Attention is all you need", "Bert Paper"])

style_input=st.selectbox("Select a style", ["Summary", "Bullet Points", "Key Takeaways"])

length_input=st.selectbox("Select length", ["Short", "Medium", "Long"])

template=PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True,
    template="Summarize the paper {paper_input} in {style_input} style with {length_input} length."
)



if st.button('Summarize'):
    chain=template | model

    result=chain.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
    })
    st.write(result.content)