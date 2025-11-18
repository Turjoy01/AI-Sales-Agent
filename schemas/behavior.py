from pydantic import BaseModel, Field
from typing import List


class BehaviorPredictionResponse(BaseModel):
    likelihood_to_buy: int = Field(..., ge=0, le=100)
    ideal_pricing_usd: float
    best_outreach_time: str
    predicted_objections: List[str]
    reasoning: str