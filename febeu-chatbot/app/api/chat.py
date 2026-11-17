from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.retriever import retriever_knowledge

router = APIRouter()

class ChatRequest(BaseModel):
    question : str

@router.post("/ask")
def ask_question(chat_request: ChatRequest):
    query = chat_request.question
    result = retriever_knowledge(query, 5)
    return result


