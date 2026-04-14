from fastapi import APIRouter
from app.services.llm_service import ask_llm

router = APIRouter()

@router.post("/chat")
def chat(message: str):
    prompt = f"""
    You are a helpful AI assistant.

    User: {message}
    """
    return {"response": ask_llm(prompt)}
