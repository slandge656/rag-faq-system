from fastapi import FastAPI, HTTPException, Depends
from app.db import documents_collection
from app.schemas import DocumentCreate
from app.auth import security, decode_access_token
from app.utils import add_to_index, search_similar, generate_answer

app = FastAPI()

@app.get("/health/")
def health_check():
    return {"status": "ok"}

@app.post("/documents/")
def upload_document(doc: DocumentCreate):
    document = {
        "content": doc.content,
        "metadata": doc.metadata or {}
    }
    result = documents_collection.insert_one(document)
    doc_id = str(result.inserted_id)
    add_to_index(doc_id, doc.content)
    return {"id": doc_id, "message": "Document uploaded and indexed successfully"}

@app.get("/documents/")
def list_documents():
    documents = list(documents_collection.find({}, {"_id": 1, "content": 1}))
    return [{"id": str(doc["_id"]), "content": doc["content"]} for doc in documents]

@app.post("/query/")
def query_document(query: str):
    results = search_similar(query)
    if not results:
        return {"query": query, "answer": "No relevant documents found."}
    answer = generate_answer(query, results)
    return {"query": query, "answer": answer}

@app.get("/secure-endpoint/")
def secure_endpoint(token: str = Depends(security)):
    decoded = decode_access_token(token.credentials)
    return {"message": "Secure access granted", "user": decoded["user"]}