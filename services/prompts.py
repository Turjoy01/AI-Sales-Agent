# services/prompts.py
LEAD_SCORING_PROMPT = """You are an expert B2B sales qualifier.

Return ONLY valid JSON with these exact keys:
{
  "score": 0-100,
  "qualification": "Hot" or "Warm" or "Cold",
  "reasoning": "explain in 1-2 sentences",
  "recommended_action": "what to do next"
}

Lead data:
{data}

Important: Return ONLY the JSON. No markdown, no extra text."""

BEHAVIOR_PREDICTION_PROMPT = """Predict buyer behavior from the lead data.

Return ONLY valid JSON:
{
  "likelihood_to_buy: 0-100,
  ideal_pricing_usd: number,
  best_outreach_time: "string",
  predicted_objections: ["string"],
  reasoning: "string"
}

Data:
{data}"""

OBJECTION_HANDLER_PROMPT = """Customer said: "{objection}"

Return ONLY valid JSON:
{{
  "short": "1-2 sentence reply",
  "medium": "3-5 sentences",
  "empathetic_long": "warm & understanding response",
  "suggested_questions": ["Q1", "Q2"]
}}"""

MEETING_SUMMARY_PROMPT = """Meeting transcript:
{transcript}

Convert to structured CRM notes. Return ONLY valid JSON:
{{
  "summary": "3-5 sentences",
  "key_decisions": ["..."],
  "action_items": [{{"task": "...", "owner": "...", "due": "..."}}],
  "sentiment": "Positive" | "Neutral" | "Negative",
  "next_steps": ["..."],
  "crm_notes": "bullet points ready to paste"
}}"""