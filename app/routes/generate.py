from fastapi import APIRouter
from app.services.llm_service import ask_llm

router = APIRouter()

@router.post("/generate")
def generate_content(topic: str):
    prompt = f"""
    Write a short engaging content about:

    {topic}

    Keep it under 120 words.
    """

    return ask_llm(prompt)
