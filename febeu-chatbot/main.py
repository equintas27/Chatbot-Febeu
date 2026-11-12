from fastapi import FastAPI
from app.api.get_connection import router

app = FastAPI(
    title="FEBEU Chatbot API",
    description="API do chatbot institucional da FEBEU",
    version="0.1.0"

)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "FEBEU Chatbot API está operacional!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
