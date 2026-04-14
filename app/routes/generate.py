from fastapi import APIRouter
from app.services.generate_service import generate_content
from app.utils.response import success, error

router = APIRouter()

@router.post("/generate")
def generate(topic: str):
    if not topic or len(topic) < 3:
        return error("Invalid topic")

    result = generate_content(topic)
    return success(result)
