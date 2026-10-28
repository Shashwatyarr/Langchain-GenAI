import os

from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY", "").strip()
if not api_key:
    raise RuntimeError("GROQ_API_KEY is not set")

model = ChatGroq(
    model="qwen/qwen3.8-27b",
    api_key=api_key,
    temperature=0,
    max_tokens=200,
)
parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age, and city of a fictional person.\n{format_instructions}",
    input_variables=[],
    partial_variables={
        "format_instructions": parser.get_format_instructions(),
    },
)

chain = template | model | parser
result = chain.invoke({})

print(result)# this is a dict
print(result['name'])
