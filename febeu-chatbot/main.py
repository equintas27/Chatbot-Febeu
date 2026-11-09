from fastapi import FastAPI

app = FastAPI(
    title="FEBEU Chatbot API",
    description="API do chatbot institucional da FEBEU",
    version="0.1.0"

)

@app.get("/")
def root():
    return {"message": "FEBEU Chatbot API está operacional!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
