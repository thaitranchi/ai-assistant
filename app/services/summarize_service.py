from app.services.llm_service import ask_llm
from app.utils.prompt_builder import build_prompt


def summarize_text(text: str) -> str:
    """
    Summarize input text into concise bullet points.
    """

    # 🔒 Validation
    if not text or len(text.strip()) < 5:
        return "Invalid input: text is too short."

    # 🧠 Build prompt (standardized)
    prompt = build_prompt(
        task="Summarize the content into 3 concise bullet points",
        content=text
    )

    try:
        # 🚀 Call LLM
        response = ask_llm(prompt)
        return response

    except Exception as e:
        # ❗ Fallback safety
        return "Failed to summarize content. Please try again later."
