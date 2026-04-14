from fastapi import APIRouter, Request
from pydantic import BaseModel, Field
import logging

from app.services.llm_service import ask_llm
from app.services.summarize_service import summarize_text
from app.services.generate_service import generate_content
from app.services.agent_router import route_task
from app.services.memory_service import get_history, save_message
from app.utils.response import success, error

router = APIRouter()


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)
    session_id: str = Field(..., min_length=1)


@router.post("/chat")
def chat(request: Request, body: ChatRequest):
    message = body.message.strip()

    try:
        # 🧠 Load history
        history = get_history(body.session_id)

        # 💾 Save user message
        save_message(body.session_id, "user", message)

        task = route_task(message)

        # 🎯 Tool routing
        if task == "summarize":
            result = summarize_text(message)

        elif task == "generate":
            result = generate_content(message)

        else:
            # 🧠 Build context-aware prompt
            context = "\n".join(
                [f"{m['role']}: {m['content']}" for m in history]
            )

            prompt = f"""
You are a professional AI assistant.

Conversation history:
{context}

User:
{message}

Respond clearly and concisely.
"""

            result = ask_llm(prompt)

        # 💾 Save AI response
        save_message(body.session_id, "assistant", str(result))

        return success({
            "task": task,
            "response": result,
            "history_length": len(get_history(body.session_id))
        })

    except Exception as e:
        logging.error("Chat error", exc_info=True)
        return error("Failed to process chat request")
