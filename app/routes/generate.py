from fastapi import APIRouter
from app.services.llm_service import ask_llm

router = APIRouter()

@router.post("/generate")
def generate(topic: str):
    messages = [
        {"role": "system", "content": "Generate a short response or content"},
        {"role": "user", "content": topic}
    ]
    return {"result": ask_llm(messages)}
