from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnablePassthrough
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
import os

load_dotenv()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Give the sentiment of the feedback"
    )

parser2=PydanticOutputParser(pydantic_object=Feedback)    

prompt1 = PromptTemplate(
    template="Classify the following feedback as positive or negative. "
    "Return the result in the requested format.\n\n"
    "Feedback: {feedback}\n{format_instruction}",
    input_variables=["feedback"],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template="The user gave positive feedback: {feedback}\n"
    "Thank them and briefly acknowledge the positive points.",
    input_variables=["feedback"],
)

prompt3 = PromptTemplate(
    template="The user gave negative feedback: {feedback}\n"
    "Apologize, acknowledge their concerns, and briefly explain that "
    "the feedback will help improve the experience.",
    input_variables=["feedback"],
)

model = ChatGroq(
    model="qwen/qwen3.8-27b",
    api_key=os.getenv("GROQ_API_KEY"),
    max_tokens=200,
)

parser = StrOutputParser()

sentiment_chain = prompt1 | model | parser2
positive_chain = prompt2 | model | parser
negative_chain = prompt3 | model | parser

conditional_chain = (
    RunnablePassthrough.assign(sentiment=sentiment_chain)
    | RunnableBranch(
        (
            lambda inputs: inputs["sentiment"].sentiment == "positive",
            positive_chain,
        ),
        negative_chain,
    )
)

feedback = """
Tatti app hai
"""

result = conditional_chain.invoke({"feedback": feedback})

print(result)
