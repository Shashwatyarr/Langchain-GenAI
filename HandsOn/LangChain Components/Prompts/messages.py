from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY", "").strip()

model = ChatGroq(
    model="qwen/qwen3.8-27b",
    api_key=api_key,
    max_tokens=200,
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of India?"),]

response = model.invoke(messages)
messages.append(AIMessage(content=response.content))

print(messages)