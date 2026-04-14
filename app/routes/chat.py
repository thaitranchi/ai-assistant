from fastapi import APIRouter
from app.services.llm_service import ask_llm

router = APIRouter()

@router.post("/chat")
def chat(message: str):
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant"},
        {"role": "user", "content": message}
    ]
    return {"response": ask_llm(messages)}
