import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from config.config import *
from preprocessing.to_text_conversion import row_to_text
from retrieval.embedder import load_embedder
from retrieval.retrieval import build_faiss_index, search_index
from utilities.data_help import load_csv
from generation.generator import generate_gemini

# Load data
data = load_csv(f"{DATA_DIR}/Training Dataset.csv")

# Preprocess
docs = [row_to_text(row) for _, row in data.iterrows()]

# Embeddings
embedder = load_embedder(MODEL_NAME)
doc_embeddings = embedder.encode(docs)
index = build_faiss_index(doc_embeddings)

# RAG QA
def answer_query(query):
    query_embedding = embedder.encode([query])
    indices = search_index(index, query_embedding, k=TOP_K)
    retrieved_docs = [docs[i] for i in indices]
    context = "\n".join(retrieved_docs)

    prompt = f"""
    You are a helpful assistant analyzing loan applications.

    Based on the following data:\n{context}\n

    Answer this question: {query}
    """

    return generate_gemini(prompt)

# Sample query
print(answer_query("What are the traits of applicants who got their loans approved?"))
