from fastapi import APIRouter, Request
from pydantic import BaseModel, Field

from app.services.summarize_service import summarize_text
from app.utils.response import success, error

router = APIRouter()


class SummarizeRequest(BaseModel):
    text: str = Field(..., min_length=5, description="Text to summarize")


@router.post("/summarize")
def summarize(request: Request, body: SummarizeRequest):
    try:
        result = summarize_text(body.text)
        return success(result)

    except Exception:
        return error("Failed to summarize text")
