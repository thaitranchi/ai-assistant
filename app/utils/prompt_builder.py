def build_prompt(task: str, content: str):
    return f"""
You are a professional AI assistant.

Task:
{task}

Content:
{content}

Rules:
- Be clear and concise
- Return structured output
"""
