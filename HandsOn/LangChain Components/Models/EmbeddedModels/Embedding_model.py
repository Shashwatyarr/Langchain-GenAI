from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY', "").strip()

embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview",
    google_api_key=api_key,
    output_dimensionality=7,
)

embedding = embedding_model.embed_query("Delhi is the capital of India")
print(embedding)



