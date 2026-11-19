import time
from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.retriever import retriever_knowledge
from app.llm.provider import FEBEUGenerator

router = APIRouter()

class ChatRequest(BaseModel):
    question : str

@router.post("/ask")
def ask_question(chat_request: ChatRequest):
    start = time.perf_counter()
    
    query = chat_request.question

    generator = FEBEUGenerator()

    result = retriever_knowledge(query, 5)

    start_g = time.perf_counter()
    response = generator.generate_response(query, result["documents"][0])
    end_g = time.perf_counter()
    print (f"Duration Gemini: {end_g - start_g}")
    end = time.perf_counter()
    duration = end - start
    return {
        "question": query,
        "answer": response
    }


