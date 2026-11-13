from pathlib import Path
import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch
from langchain_groq import ChatGroq

load_dotenv(dotenv_path=Path(__file__).resolve().with_name(".env"))

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is not set in the .env file beside this script.")

model = ChatGroq(model="qwen/qwen3.8-27b", api_key=api_key, max_tokens=200)
parser = StrOutputParser()

refund_chain = (
    PromptTemplate.from_template(
        "Reply helpfully to this customer asking for a refund: {query}"
    )
    | model
    | parser
)

general_chain = (
    PromptTemplate.from_template(
        "Reply helpfully to this customer support message: {query}"
    )
    | model
    | parser
)

branch = RunnableBranch(
    (lambda x: "refund" in x["query"].lower(), refund_chain),
    general_chain,
)

if __name__ == "__main__":
    result = branch.invoke({"query": "I want a refund for my order."})
    print(result)
