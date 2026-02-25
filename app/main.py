from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.llm import ask_llm

app = FastAPI(
    title="LLM Chat API",
    description="Lightweight AI chat backend powered by Groq",
    version="1.0.0",
)

# Request model
class ChatRequest(BaseModel):
    message: str


# Root endpoint
@app.get("/")
def root():
    return {"message": "LLM Chat API is running"}


# Health check endpoint
@app.get("/health")
def health():
    return {"status": "ok"}


# Chat endpoint
@app.post("/chat")
def chat(request: ChatRequest):
    try:
        response = ask_llm(request.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))