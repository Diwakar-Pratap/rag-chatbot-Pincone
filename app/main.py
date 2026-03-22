from fastapi import FastAPI
from app.schemas.request import QueryRequest
from app.rag.pipeline import rag_chat
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# ✅ FIRST create app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "RAG chatbot running"}

@app.post("/chat")
def chat(request: QueryRequest):
    answer = rag_chat(request.question)
    return {"answer": answer}