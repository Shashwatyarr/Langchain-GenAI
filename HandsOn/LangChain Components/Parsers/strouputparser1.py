import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

model= ChatGroq(model='qwen/qwen3.8-27b', api_key=api_key,max_tokens=200)


template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"],
)

template2 = PromptTemplate(
    template="Write a 5 line summary on the following text:\n{text}",
    input_variables=["text"],
)

parser=StrOutputParser()

chain=template1|model|parser|template2|model|parser

result=chain.invoke({'topic':'black hole'})

print(result)