# routers/ai_agent.py
from fastapi import APIRouter, File, UploadFile, HTTPException
from schemas.lead import LeadScoreRequest, LeadScoreResponse
from schemas.behavior import BehaviorPredictionResponse
from schemas.objection import ObjectionRequest, ObjectionResponse
from schemas.meeting import MeetingResponse
from services.ollama_service import ollama_chat
from services.whisper_local import transcribe_audio
import json
import re

router = APIRouter(prefix="/ai-agent", tags=["AI Sales Agent"])


def extract_json(text: str) -> str:
    """Extract clean JSON from Ollama response (removes markdown, extra text)"""
    text = text.strip()
    text = re.sub(r"^```json\s*|```$", "", text, flags=re.MULTILINE)
    start = text.find("{")
    end = text.rfind("}") + 1
    if start == -1 or end == 0:
        raise ValueError("No JSON object found in Ollama response")
    return text[start:end]


@router.post("/lead-score", response_model=LeadScoreResponse)
async def lead_score(req: LeadScoreRequest):
    data_json = json.dumps(req.dict(), indent=2, ensure_ascii=False)
    user_prompt = f"""You are a B2B sales qualification expert.

Return ONLY this exact JSON (no markdown, no extra text):
{{
  "score": 0-100,
  "qualification": "Hot" or "Warm" or "Cold",
  "reasoning": "1-2 sentences",
  "recommended_action": "next step"
}}

Lead data:
{data_json}"""

    raw = await ollama_chat(
        system="You are a strict JSON API. Never add explanations.",
        user=user_prompt,
        temperature=0.1
    )
    try:
        return json.loads(extract_json(raw))
    except Exception as e:
        raise HTTPException(500, f"Invalid JSON from Ollama:\n{raw}\nError: {e}")


@router.post("/predict-behavior", response_model=BehaviorPredictionResponse)
async def predict_behavior(req: LeadScoreRequest):
    data_json = json.dumps(req.dict(), indent=2, ensure_ascii=False)
    user_prompt = f"""Predict buyer behavior based on this lead.

Return ONLY valid JSON:
{{
  "likelihood_to_buy": 0-100,
  "ideal_pricing_usd": 0.0,
  "best_outreach_time": "string (e.g. Tuesday 10am)",
  "predicted_objections": ["string"],
  "reasoning": "string"
}}

Data:
{data_json}"""

    raw = await ollama_chat(system="Return only JSON", user=user_prompt, temperature=0.2)
    return json.loads(extract_json(raw))


@router.post("/objection-handler", response_model=ObjectionResponse)
async def objection_handler(req: ObjectionRequest):
    user_prompt = f"""Customer said: "{req.objection}"

Return ONLY this JSON:
{{
  "short": "1-2 sentence reply",
  "medium": "3-5 sentences",
  "empathetic_long": "warm and understanding response",
  "suggested_questions": ["Question 1", "Question 2"]
}}"""

    raw = await ollama_chat(system="Return only JSON", user=user_prompt)
    return json.loads(extract_json(raw))


@router.post("/meeting-transcribe", response_model=MeetingResponse)
async def meeting_transcribe(file: UploadFile = File(...)):
    allowed = ('.mp3', '.wav', '.m4a', '.ogg', '.webm', '.mp4')
    if not file.filename.lower().endswith(allowed):
        raise HTTPException(400, "Please upload an audio/video file")

    audio_bytes = await file.read()
    transcript = transcribe_audio(audio_bytes)

    user_prompt = f"""Meeting transcript:
{transcript}

Return ONLY valid JSON with this structure:
{{
  "summary": "3-5 sentence summary",
  "key_decisions": ["decision 1", "decision 2"],
  "action_items": [{{"task": "string", "owner": "string", "due": "string"}}],
  "sentiment": "Positive" or "Neutral" or "Negative",
  "next_steps": ["step 1", "step 2"],
  "crm_notes": "bullet points ready to paste into CRM"
}}"""

    raw = await ollama_chat(
        system="You are a CRM assistant. Return only JSON.",
        user=user_prompt,
        temperature=0.1
    )
    return json.loads(extract_json(raw))