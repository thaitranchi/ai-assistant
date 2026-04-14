from fastapi import FastAPI
from app.routes import chat, summarize, generate

app = FastAPI(title="AI Support Assistant API")

app.include_router(chat.router, prefix="/v1")
app.include_router(summarize.router, prefix="/v1")
app.include_router(generate.router, prefix="/v1")
app.include_router(health.router, prefix="/v1")

@app.get("/")
def root():
    return {"message": "AI Assistant Running"}
