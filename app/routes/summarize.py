from fastapi import APIRouter
from app.services.llm_service import ask_llm
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import Request

limiter = Limiter(key_func=get_remote_address)
router = APIRouter()

def error(msg):
    return {"status": "error", "message": msg}
    
@router.post("/summarize")
@limiter.limit("5/minute")
def summarize_text(text: str):
    if not text or len(text) < 3:
        return error("Invalid text")
    prompt = f"""
    Summarize the following text into 3 concise bullet points.

    Text:
    {text}

    Output:
    - Point 1
    - Point 2
    - Point 3
    """

    return ask_llm(prompt)
