from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY", "").strip()

model = ChatGroq(
    model="qwen/qwen3.8-27b",
    api_key=api_key,
    max_tokens=200,
)

chat_history=[
    SystemMessage(content="You are a helpful assistant."),
]

while True:
    user_input = input("User: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break

    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(f"AI: {response.content}")

print("Exiting the chat. Goodbye!")    