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

logging.basicConfig(level=logging.INFO)

def ask_llm(prompt: str):
    logging.info(f"Input: {prompt[:50]}")
    for attempt in range(3):
        try:
            return success(gemini_call(prompt))
        except Exception as e:
            logging.error("Gemini failed", exc_info=True)
            print(error(f"Attempt {attempt+1} failed:", e))
            time.sleep(2 ** attempt)

    # fallback
    try:
        return success(openrouter_call(prompt))
    except:
        return fallback_response(prompt)
