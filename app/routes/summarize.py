from fastapi import APIRouter
from app.services.llm_service import ask_llm

router = APIRouter()

@router.post("/summarize")
def summarize_text(text: str):
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
