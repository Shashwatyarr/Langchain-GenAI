#isse kisi bhi function ko runnable me convert kar sakte hai. Runnable me convert karne ke baad usse parallel ya sequentially run kar sakte hai kisi bhi chain me.
from pathlib import Path

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel,RunnableLambda,RunnablePassthrough  
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=Path(__file__).resolve().with_name(".env"))

prompt1 = PromptTemplate(
    template='Generate a tweet on {text}',
    input_variables=['text'],
)


api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is not set. Add it to your environment or .env file.")

model = ChatGroq(model="qwen/qwen3.8-27b", api_key=api_key, max_tokens=200)

parser=StrOutputParser()

tweet_gen_chain=RunnableSequence(prompt1,model,parser)

def word_count(text):
    return len(text.split())

parallel_chain=RunnableParallel({
    'tweet':RunnablePassthrough(),
    'word count':RunnableLambda(word_count)  # Example lambda function
}
)

final_chain=RunnableSequence(tweet_gen_chain,parallel_chain)

print(final_chain.invoke({
    'text': 'Agentic AI'
}))