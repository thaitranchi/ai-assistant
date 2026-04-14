from app.services.llm_service import ask_llm
from app.utils.prompt_builder import build_prompt

def summarize_text(text: str):
    prompt = build_prompt(
        "Summarize into 3 bullet points",
        text
    )
    return ask_llm(prompt)
