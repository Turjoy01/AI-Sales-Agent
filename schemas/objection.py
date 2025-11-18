from pydantic import BaseModel
from typing import List


class ObjectionRequest(BaseModel):
    objection: str
    context: str = "B2B SaaS platform for European multi-vendor sales"


class ObjectionResponse(BaseModel):
    short: str
    medium: str
    empathetic_long: str
    suggested_questions: List[str]