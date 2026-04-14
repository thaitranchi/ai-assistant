from fastapi import APIRouter
from app.services.llm_service import ask_llm
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import Request

limiter = Limiter(key_func=get_remote_address)
router = APIRouter()

@router.post("/generate")
@limiter.limit("5/minute")
def generate_content(topic: str):
    prompt = f"""
    Write a short engaging content about:

    {topic}

    Keep it under 120 words.
    """

    return ask_llm(prompt)
