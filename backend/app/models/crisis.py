from pydantic import BaseModel
from typing import List, Dict, Any

class Crisis(BaseModel):
    id: str
    name: str
    location: str
    start_date: str
    end_date: str
    cause_tags: List[str]
    metrics: Dict[str, Any]