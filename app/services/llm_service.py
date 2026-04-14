from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_llm(prompt: str):
    full_prompt = f"""
    You are an AI assistant for automation systems.
    Be concise, clear, and structured.

    User request:
    {prompt}
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
