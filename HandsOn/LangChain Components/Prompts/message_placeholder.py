from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} assistant."),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', "{query}")])

chat_history=[]

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)  

chat_template = chat_template.invoke({'domain':'AI', 'query':"LangChain", 'chat_history':chat_history})


print(chat_template)