from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from enum import Enum
from datetime import date


class CrisisStatus(str, Enum):
    ACTIVE = "active"
    RESOLVED = "resolved"
    FROZEN = "frozen"
    ESCALATING = "escalating"


class CasualtiesRange(BaseModel):
    low: int
    high: int
    confidence: str


class Displacement(BaseModel):
    idp: int
    refugees: int
    unit: str = "millions"


class KeyEvent(BaseModel):
    date: str  # ISO date string
    description: str
    type: str


class InternationalResponse(BaseModel):
    un_involved: bool
    sanctions: bool
    peacekeepers: int


class Crisis(BaseModel):
    name: str
    crisis_id: str
    start_date: str  # ISO date
    end_date: Optional[str] = None
    duration_years: Optional[float] = None
    status: CrisisStatus
    casualties_range: CasualtiesRange
    displacement: Displacement
    regions_affected: List[str]
    cause_tags: List[str]
    key_events: List[KeyEvent]
    resolution_mechanism: Optional[str] = None
    international_response: Optional[InternationalResponse] = None
    data_sources: List[str]
    last_updated: str
