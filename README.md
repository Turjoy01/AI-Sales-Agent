Here’s the **perfect, professional, GitHub-ready `README.md`** that matches **exactly** your current project structure (including the `__pycache__` folders you showed — we’ll ignore those in the README of course).

Copy-paste this directly into your project root as `README.md`:

```markdown
# AI Sales Agent – 100% Local, Private & Offline

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-brightgreen)
![Ollama](https://img.shields.io/badge/Ollama-Llama3.1%208B-orange)
![Whisper](https://img.shields.io/badge/Whisper-Local_CPU-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)

A **fully offline**, high-performance AI Sales Assistant powered by **Ollama** and **local OpenAI Whisper**.  
No OpenAI API · No cloud · No data leaks · Zero recurring cost.

Live interactive docs: http://127.0.0.1:8000/docs

## What It Can Do (All in < 10 seconds)

| Input                         | Instant AI Output                                           |
|-------------------------------|---------------------------------------------------------------|
| Lead details (JSON)           | Lead score, qualification, reasoning, next best action       |
| Same lead                     | Buy probability, ideal price, best contact time, objections  |
| Customer objection            | 3-tier response + discovery questions                         |
| Sales call recording (audio)  | Transcript + AI summary + action items + CRM-ready notes      |

Perfect for B2B SaaS, marketplaces, reseller networks, and agencies.

## API Endpoints

```http
POST /ai-agent/lead-score
POST /ai-agent/predict-behavior
POST /ai-agent/objection-handler
POST /ai-agent/meeting-transcribe   (multipart audio upload)
```

Swagger UI: http://127.0.0.1:8000/docs  
Redoc: http://127.0.0.1:8000/redoc

## Tech Stack (All Local)

| Layer               | Technology                         | Notes                              |
|---------------------|------------------------------------|------------------------------------|
| Framework           | FastAPI                            | Async, auto-docs                   |
| LLM                 | Ollama (`llama3.1:8b` recommended) | Fully private, runs on CPU/GPU     |
| Speech-to-Text      | OpenAI Whisper (local)             | CPU-only, no PyAV compilation     |
| Audio Formats       | .mp3, .wav, .m4a, .ogg, .webm      | FFmpeg bundled                     |
| JSON Parsing        | Strict prompts + robust extraction | Works even with ```json blocks     |

Tested & stable on **Windows 10/11 (CPU only)** · Works on Linux/macOS too.

## Project Structure

```
AI-SALES-AGENT-OLLAMA/
├── main.py
├── routers/
│   └── ai_agent.py              # All 4 endpoints
├── schemas/
│   ├── lead.py
│   ├── behavior.py
│   ├── objection.py
│   └── meeting.py
├── services/
│   ├── ollama_service.py        # Ollama chat wrapper
│   ├── prompts.py               # Prompt engineering
│   └── whisper_local.py         # Local Whisper transcription
├── .env.example
├── requirements.txt
└── README.md                    # ← you are here
```

## Quick Start

```bash
# 1. Install Ollama
# https://ollama.com/download

# 2. Download the model (once)
ollama pull llama3.1:8b

# 3. Setup Python
git clone 
cd AI-SALES-AGENT-OLLAMA
python -m venv .venv
.\.venv\Scripts\activate        # Windows
# source .venv/bin/activate     # macOS/Linux

pip install -r requirements.txt

# 4. Run
uvicorn main:app --reload
```

Open → http://127.0.0.1:8000/docs → Test all 4 endpoints instantly!

## Example Requests

See the Swagger UI or check the `examples/` folder (I can create it for you with sample JSON + test audio).

## Upcoming Features (Ready to Add)

- API key authentication + multi-tenant support (SaaS-ready)
- SQLite/PostgreSQL logging
- Beautiful drag-and-drop HTML dashboard
- Webhooks to HubSpot, Salesforce, Pipedrive
- One-click deployment (Railway, Render, Fly.io)

---

**Your leads. Your recordings. Your AI. 100% under your control.**

Built for speed, privacy, and real sales teams.

Star this repo if you like it!  
Contributions · Issues · Feature requests welcome

Made with Turjoy❤️