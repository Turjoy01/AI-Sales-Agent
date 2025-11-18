from pydantic import BaseModel, Field
from typing import Optional


class LeadScoreRequest(BaseModel):
    company_name: str = Field(..., description="Company name")
    job_title: str = Field(..., description="Contact job title")
    website: Optional[str] = None
    email: str = Field(..., description="Contact email")
    annual_revenue: Optional[float] = None
    employee_count: Optional[int] = None
    industry: str = Field(..., description="Industry sector")
    previous_interactions: Optional[str] = ""
    pain_points: Optional[str] = None


class LeadScoreResponse(BaseModel):
    score: int = Field(..., ge=0, le=100, description="Lead score 0-100")
    qualification: str = Field(..., description="Hot / Warm / Cold")
    reasoning: str = Field(..., description="Why this score")
    recommended_action: str = Field(..., description="Next step for sales rep")