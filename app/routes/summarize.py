from fastapi import APIRouter, Request
from pydantic import BaseModel

from app.services.summarize_service import summarize_text
from app.utils.response import success, error

router = APIRouter()


# 📥 Request schema (chuẩn hóa input)
class SummarizeRequest(BaseModel):
    text: str


# 🚀 Endpoint
@router.post("/summarize")
def summarize(request: Request, body: SummarizeRequest):
    text = body.text

    # 🔒 Validation
    if not text or len(text.strip()) < 5:
        return error("Invalid text. Must be at least 5 characters.")

    try:
        result = summarize_text(text)
        return success(result)

    except Exception:
        return error("Failed to process summarization request.")
