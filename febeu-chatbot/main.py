from fastapi import FastAPI
from app.api.get_connect import router as connect_router
from app.api.health import router as health_router

app = FastAPI(
    title="FEBEU Chatbot API",
    description="API do chatbot institucional da FEBEU",
    version="0.1.0"
)

app.include_router(connect_router)
app.include_router(health_router)
