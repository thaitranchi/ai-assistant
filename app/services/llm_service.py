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

def success(data):
    return {"status": "success", "data": data}

def error(msg):
    return {"status": "error", "message": msg}
    
def fallback_response(prompt: str):
    return f"[Fallback AI] Simulated response: {prompt[:50]}..."

import time
import logging
from app.services.llm_openrouter import openrouter_call

logging.basicConfig(level=logging.INFO)

def fallback_response():
    return "AI service is temporarily unavailable. Please try again later."


def ask_llm(prompt: str):
    for attempt in range(3):
        try:
            logging.info(f"Calling Gemini, attempt {attempt+1}")
            return gemini_call(prompt)
        except Exception as e:
            logging.error(f"Gemini error: {e}")
            time.sleep(2 ** attempt)

    try:
        logging.info("Fallback to OpenRouter")
        return openrouter_call(prompt)
    except Exception as e:
        logging.error(f"OpenRouter error: {e}")
        return fallback_response()
