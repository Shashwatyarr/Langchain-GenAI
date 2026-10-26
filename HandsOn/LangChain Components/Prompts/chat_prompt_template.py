from langchain_core.prompts import ChatPromptTemplate

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} assistant."),
    ('human', "What is the {topic}?"),
])

prompt = chat_template.invoke({'domain':'AI', 'topic':"LangChain"})

print(prompt.messages)