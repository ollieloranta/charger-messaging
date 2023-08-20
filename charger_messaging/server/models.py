from typing import List
from pydantic import BaseModel


class Session(BaseModel):
    session_id: int
    energy_kwh: int
    duration_s: int
    cost_cents: int


class ManySessions(BaseModel):
    sessions: List[Session]
