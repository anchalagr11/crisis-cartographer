from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class ComparisonRequest(BaseModel):
    crisis_ids: List[str]

class ComparisonMetrics(BaseModel):
    tag_similarity: float
    timeline_overlap: float
    casualty_ratio: float
    displacement_ratio: float
    duration_delta_years: float
    geospatial_metrics: Optional[Dict[str, Any]] = None

class ComparisonResult(BaseModel):
    crisis_a: str
    crisis_b: str
    metrics: ComparisonMetrics
    key_similarities: List[str] = []
    key_differences: List[str] = []
    contextual_significance: Optional[str] = None
    data_limitations: List[str] = []
    aligned_events: Dict[str, List[Dict[str, Any]]] = {}
    region_coordinates: Dict[str, Dict[str, Any]] = {}
    recommendations: Dict[str, List[Dict[str, Any]]] = {}
    forecasts: Dict[str, Dict[str, Any]] = {}