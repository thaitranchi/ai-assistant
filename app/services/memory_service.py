memory_store = {}


def get_history(session_id: str):
    return memory_store.get(session_id, [])


def save_message(session_id: str, role: str, content: str):
    if session_id not in memory_store:
        memory_store[session_id] = []

    memory_store[session_id].append({
        "role": role,
        "content": content
    })

    # limit history (tránh token quá dài)
    memory_store[session_id] = memory_store[session_id][-10:]
