from fastapi import APIRouter, Request
from pydantic import BaseModel, Field

from app.services.llm_service import ask_llm
from app.services.summarize_service import summarize_text
from app.services.generate_service import generate_content
from app.services.agent_router import route_task
from app.utils.response import success, error

router = APIRouter()


# 📥 Request schema
class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)

# 🚀 Endpoint
@router.post("/chat")
def chat(request: Request, body: ChatRequest):
    message = body.message

    if not message or len(message.strip()) == 0:
        return error("Message is required")

    try:
        task = route_task(message)

        if task == "summarize":
            result = summarize_text(message)

        elif task == "generate":
            result = generate_content(message)

        else:
            # Default AI chat
            prompt = f"""
You are a helpful AI assistant.

User:
{message}

Answer clearly and concisely.
"""
            result = ask_llm(prompt)

        return success({
            "task": task,
            "response": result
        })

    except Exception:
        return error("Failed to process chat request")
