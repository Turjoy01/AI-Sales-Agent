from fastapi import FastAPI
from routers import ai_agent

app = FastAPI(
    title="AI Sales Agent Tools (Ollama Local)",
    description="Fully offline AI backend - Lead scoring, Behavior prediction, Objection handling, Meeting notes",
    version="1.0.0"
)

app.include_router(ai_agent.router)

@app.get("/")
def home():
    return {"status": "AI Sales Agent running locally with Ollama!", "docs": "/docs"}