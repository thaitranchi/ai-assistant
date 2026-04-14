def route_task(message: str):
    msg = message.lower()

    if "summarize" in msg:
        return "summarize"
    elif "generate" in msg or "write" in msg:
        return "generate"
    return "chat"
