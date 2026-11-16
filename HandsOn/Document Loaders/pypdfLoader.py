from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
load_dotenv()

model=ChatGroq(model="qwen/qwen3.8-27b",api_key=os.getenv("GROQ_API_KEY"))

prompt=PromptTemplate(
    template='write a real summary(dont write the poem again) poem about {poem}',
    input_variables=['poem']
)

parser=StrOutputParser()

loader =PyPDFLoader("HandsOn\\Document Loaders\\internship_presentation.pdf",encoding="utf-8")

docs=loader.load()

chain=prompt|model|parser

print(chain.invoke({'poem':docs[0].page_content}))