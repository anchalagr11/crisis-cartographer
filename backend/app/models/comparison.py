from pydantic import BaseModel
from typing import List

class ComparisonRequest(BaseModel):
    crisis_ids: List[str]

class ComparisonResult(BaseModel):
    similarities: dict
    differences: dict