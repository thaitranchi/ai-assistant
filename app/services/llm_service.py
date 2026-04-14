import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def ask_llm(prompt: str):
    full_prompt = f"""
    You are an AI assistant for automation systems.
    Be concise, clear, and structured.

    User request:
    {prompt}
    """
    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
