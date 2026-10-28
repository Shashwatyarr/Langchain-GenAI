#pydantic me strict schema enforcement ke sath sath structured output krr skte hai toh ye best rehta h

import os

from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field

load_dotenv()

api_key = os.getenv("GROQ_API_KEY", "").strip()
if not api_key:
    raise RuntimeError("GROQ_API_KEY is not set")


class Person(BaseModel):
    name: str = Field(description="Name of a person")
    age: int = Field(description="age of the person")
    city: str = Field(description="Name of the city a person lives in")


model = ChatGroq(
    model="qwen/qwen3.8-27b",
    api_key=api_key,
    temperature=0,
    max_tokens=200,
)
parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template=(
        "Generate the name, age, and city of a fictional {place} person.\n"
        "{format_instructions}"
    ),
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = template | model | parser
result = chain.invoke({"place": "Indian"})

print(result.model_dump())