
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY", "").strip()

llm = ChatGroq(
    model="qwen/qwen3.8-27b",
    api_key=api_key,
)

print("Calling Groq...")
response = llm.invoke("What is the capital of India?")
print(response.content)
