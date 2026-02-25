# LLM Chat API (FastAPI + Groq)

Production-ready AI chat backend built with FastAPI and Docker.

---

## Features

- REST API for LLM chat
- Modular architecture
- Environment-based configuration
- Docker support
- Health check endpoint
- Swagger documentation

---

## Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- Docker
- Groq API

---

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload