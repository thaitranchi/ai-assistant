from fastapi import APIRouter
from app.services.llm_service import ask_llm
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import Request

limiter = Limiter(key_func=get_remote_address)
router = APIRouter()

@router.post("/chat")
@limiter.limit("5/minute")
def chat(message: str):
    prompt = f"""
    You are a helpful AI assistant.

    User: {message}
    """
    return {"response": ask_llm(prompt)}
