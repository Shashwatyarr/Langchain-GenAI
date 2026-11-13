from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
import os

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic'],
)

prompt2 = PromptTemplate(
    template='Summarize the following report: {report}',
    input_variables=['report'],
)

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is not set. Add it to your environment or .env file.")

model = ChatGroq(model="qwen/qwen3.8-27b", api_key=api_key, max_tokens=200)
parser = StrOutputParser()
chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

if __name__ == "__main__":
    try:
        result = chain.invoke({'topic': 'cricket'})
        print(result)
    except Exception as exc:
        raise SystemExit(
            "Groq API call failed. Check that GROQ_API_KEY is valid and the model is available to your account."
        ) from exc