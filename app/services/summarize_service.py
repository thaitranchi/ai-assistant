from app.services.llm_service import ask_llm


def summarize_text(text: str) -> str:
    """
    Summarize input text into 3 concise bullet points.
    """

    # 🔒 Validation
    if not text or len(text.strip()) < 5:
        raise ValueError("Input text is too short")

    # 🧠 Prompt chuẩn hóa (tránh random output)
    prompt = f"""
Summarize the following text into exactly 3 concise bullet points.

Text:
{text}

Rules:
- Each point must be one line
- Keep it short and clear
- Do not add extra explanation

Format:
- Point 1
- Point 2
- Point 3
"""

    try:
        response = ask_llm(prompt)

        # 🔧 Clean output (loại bỏ khoảng trắng dư)
        return response.strip()

    except Exception as e:
        # ❗ Không expose lỗi internal
        raise RuntimeError("Failed to summarize text") from e
