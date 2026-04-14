from fastapi import APIRouter, Request
from pydantic import BaseModel, Field

from app.services.generate_service import generate_content
from app.utils.response import success, error

router = APIRouter()


class GenerateRequest(BaseModel):
    topic: str = Field(..., min_length=3, description="Topic to generate content")


@router.post("/generate")
def generate(request: Request, body: GenerateRequest):
    try:
        result = generate_content(body.topic)
        return success(result)

    except Exception:
        return error("Failed to generate content")
