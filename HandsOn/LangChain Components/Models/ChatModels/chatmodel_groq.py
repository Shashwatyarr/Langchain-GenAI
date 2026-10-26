from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY", "").strip()

model = ChatGroq(
    model="qwen/qwen3.8-27b",
    api_key=api_key,
    temperature=0,
    max_tokens=100,
)

response = model.invoke("Suggest me 5 indian male names")
print(response.content)
