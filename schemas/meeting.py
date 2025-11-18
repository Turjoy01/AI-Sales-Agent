from pydantic import BaseModel
from typing import List, Dict


class MeetingResponse(BaseModel):
    summary: str
    key_decisions: List[str]
    action_items: List[Dict[str, str]]
    sentiment: str
    next_steps: List[str]
    crm_notes: str