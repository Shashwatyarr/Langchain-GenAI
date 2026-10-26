import os

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY", "").strip() or os.getenv("GEMINI_API_KEY", "").strip()
if not api_key:
    raise RuntimeError("Set GOOGLE_API_KEY or GEMINI_API_KEY in your environment or .env file.")

documents = [
    "Delhi is the capital of India.",
    "Kolkata is the capital of West Bengal.",
    "Paris is the capital of France.",
    "Mumbai is the financial capital of India.",
    "London is the capital of the United Kingdom.",
    "Tokyo is the capital of Japan.",
    "Berlin is the capital of Germany.",
    "Rome is the capital of Italy.",
    "New Delhi is the seat of the Indian government.",
    "Chennai is the capital of Tamil Nadu.",
    "The Earth revolves around the Sun.",
    "Water freezes at zero degrees Celsius.",
    "Python is a popular programming language.",
    "C++ is widely used for competitive programming.",
    "Docker packages applications into containers.",
    "Kubernetes orchestrates containerized applications.",
    "Machine learning enables computers to learn from data.",
    "Neural networks are used in deep learning.",
    "The Himalayas are located in Asia.",
    "The Ganga is a major river in India.",
]
query = "What is the capital of Japan?"

embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview",
    google_api_key=api_key,
    output_dimensionality=768,
)
document_embeddings = embedding_model.embed_documents(documents)
query_embedding = embedding_model.embed_query(query)
similarities = cosine_similarity([query_embedding], document_embeddings)[0]
most_similar_document = documents[similarities.argmax()]

print(most_similar_document)
