from app.services.llm_service import ask_llm
from app.utils.prompt_builder import build_prompt

def generate_content(topic: str):
    prompt = build_prompt(
        "Write a short engaging content with title",
        topic
    )
    return ask_llm(prompt)
