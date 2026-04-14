from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
