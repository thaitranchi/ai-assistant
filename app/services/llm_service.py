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

import time

def ask_llm(prompt: str):
    for attempt in range(3):
        try:
            return gemini_call(prompt)
        except Exception as e:
            print(f"Attempt {attempt+1} failed:", e)
            time.sleep(2 ** attempt)

    # fallback
    try:
        return openrouter_call(prompt)
    except:
        return fallback_response(prompt)
