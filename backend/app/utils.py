import faiss
from sentence_transformers import SentenceTransformer
import numpy as np
import openai
import os
from app.db import documents_collection

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
dimension = 384
index = faiss.IndexFlatL2(dimension)

document_embeddings = []

openai.api_key = os.getenv("OPENAI_API_KEY")

def add_to_index(doc_id: str, content: str):
    embedding = model.encode(content)
    index.add(np.array([embedding]))
    document_embeddings.append((doc_id, embedding))

def search_similar(query: str, top_k=3):
    query_embedding = model.encode(query)
    distances, indices = index.search(np.array([query_embedding]), top_k)
    results = []
    for idx in indices[0]:
        if idx < len(document_embeddings):
            doc_id, _ = document_embeddings[idx]
            document = documents_collection.find_one({"_id": doc_id})
            results.append({"id": str(doc_id), "content": document["content"]})
    return results

def generate_answer(query: str, context: list):
    context_text = "\n\n".join([doc["content"] for doc in context])
    prompt = f"Answer the question based on the following context:\n\n{context_text}\n\nQuestion: {query}\nAnswer:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()