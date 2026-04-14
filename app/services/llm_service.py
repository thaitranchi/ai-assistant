from google import genai
import os
from dotenv import load_dotenv
from app.services.llm_openrouter import openrouter_call

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def gemini_call(prompt: str):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text


def fallback_response(prompt: str):
    return f"[Fallback AI] Simulated response: {prompt[:50]}..."


def ask_llm(prompt: str):
    try:
        return gemini_call(prompt)
    except Exception as e:
        print("Gemini error:", e)

        try:
            return openrouter_call(prompt)
        except Exception as e2:
            print("OpenRouter error:", e2)
            return fallback_response(prompt)
