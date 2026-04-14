from fastapi import APIRouter, Request
from pydantic import BaseModel, Field
import logging

from app.services.generate_service import generate_content
from app.utils.response import success, error

router = APIRouter()


# 📥 Request schema
class GenerateRequest(BaseModel):
    topic: str = Field(..., min_length=3, description="Topic to generate content")


@router.post("/generate")
def generate(request: Request, body: GenerateRequest):
    try:
        topic = body.topic.strip()

        logging.info(f"Generate request: {topic}")

        result = generate_content(topic)

        # 🔒 Validate output
        if not result:
            return error("Empty AI response")

        return success(result)

    except Exception as e:
        logging.error("Generate error", exc_info=True)
        return error("Failed to generate content")
