from fastapi import FastAPI
from app.routes import chat, summarize, generate

app = FastAPI(title="AI Support Assistant API")

app.include_router(chat.router)
app.include_router(summarize.router)
app.include_router(generate.router)

@app.get("/")
def root():
    return {"message": "AI Assistant Running"}
