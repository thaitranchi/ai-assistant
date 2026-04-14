from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_llm(prompt: str):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        # 🔥 fallback khi quota hết
        if "429" in str(e):
            return fallback_response(prompt)

        return f"Error: {str(e)}"


def fallback_response(prompt: str):
    return f"[Fallback AI] Simulated response for: {prompt[:50]}..."
