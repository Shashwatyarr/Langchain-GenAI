
from pathlib import Path

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=Path(__file__).resolve().with_name(".env"))

prompt1 = PromptTemplate(
    template='Generate a tweet on {text}',
    input_variables=['text'],
)

prompt2= PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text'],
)


api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is not set. Add it to your environment or .env file.")

model = ChatGroq(model="qwen/qwen3.8-27b", api_key=api_key, max_tokens=200)

parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'summary':RunnableSequence(prompt2,model,parser)
}
)

result = parallel_chain.invoke({
    'text': 'Cricket is a bat-and-ball sport played between two teams.',
})

print(result)