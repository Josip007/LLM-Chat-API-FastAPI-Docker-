from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.llm import ask_llm

app = FastAPI(
    title="LLM Chat API",
    description="Lightweight AI chat backend powered by Groq",
    version="1.0.0",
)

templates = Jinja2Templates(directory="templates")

# Request model
class ChatRequest(BaseModel):
    message: str


# Root endpoint
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

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