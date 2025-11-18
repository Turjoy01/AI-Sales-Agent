# services/ollama_service.py
import httpx
import json
import re
import os
from dotenv import load_dotenv

load_dotenv()
MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b")

async def ollama_chat(system: str, user: str, temperature: float = 0.3) -> str:
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ],
        "stream": False,
        "temperature": temperature,
        "options": {"num_ctx": 8192},
        "format": "json"                     # ← Force JSON mode
    }

    async with httpx.AsyncClient(timeout=300.0) as client:
        response = await client.post("http://localhost:11434/api/chat", json=payload)
        response.raise_for_status()
        raw_content = response.json()["message"]["content"]

        # Clean any markdown, newlines, extra spaces → pure JSON string
        cleaned = raw_content.strip()
        cleaned = re.sub(r"^```json\s*|```$", "", cleaned, flags=re.MULTILINE)  # remove ```json blocks
        cleaned = cleaned.strip()

        return cleaned