import logging
from app.services.llm_service import ask_llm
from app.utils.prompt_builder import build_prompt


def generate_content(topic: str) -> str:
    """
    Generate short engaging content with a title.
    """

    # 🔒 Validation
    if not topic or len(topic.strip()) < 3:
        raise ValueError("Topic is too short")

    # 🧠 Prompt (enforced format)
    prompt = f"""
Write a short engaging content about the topic below.

Topic:
{topic}

STRICT RULES:
- Must include a title
- Format:
Title: ...
Content: ...
- Keep it concise
"""

    try:
        response = ask_llm(prompt)

        # 🔧 Basic validation
        if not response or "Title:" not in response:
            raise ValueError("Invalid AI output")

        return response.strip()

    except Exception as e:
        logging.error("Generate content failed", exc_info=True)
        raise RuntimeError("Failed to generate content") from e
