from fastapi import APIRouter
from app.services.llm_service import ask_llm

router = APIRouter()

@router.post("/summarize")
def summarize(text: str):
    messages = [
        {"role": "system", "content": "Summarize the following text"},
        {"role": "user", "content": text}
    ]
    return {"summary": ask_llm(messages)}
