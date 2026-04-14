from typing import Any

def success(data: Any):
    return {
        "status": "success",
        "data": data
    }

def error(message: str):
    return {
        "status": "error",
        "message": message
    }
