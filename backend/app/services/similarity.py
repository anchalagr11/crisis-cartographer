from datetime import datetime
from typing import List, Set
from .normalization import normalize_date

def calculate_jaccard_similarity(set1: List[str], set2: List[str]) -> float:
    """Calculate Jaccard similarity index between two lists of tags."""
    s1 = set(set1)
    s2 = set(set2)
    intersection = len(s1 & s2)
    union = len(s1 | s2)
    return round(intersection / union, 2) if union > 0 else 0.0

def calculate_timeline_overlap(start1: str, end1: str, start2: str, end2: str) -> float:
    """Calculate temporal overlap ratio."""
    s1 = normalize_date(start1)
    e1 = normalize_date(end1) if end1 else datetime.now()
    s2 = normalize_date(start2)
    e2 = normalize_date(end2) if end2 else datetime.now()
    
    latest_start = max(s1, s2)
    earliest_end = min(e1, e2)
    
    overlap = (earliest_end - latest_start).days
    total_span = (max(e1, e2) - min(s1, s2)).days
    
    return round(max(0, overlap) / total_span, 2) if total_span > 0 else 0.0

def calculate_metric_ratio(val1: float, val2: float) -> float:
    """Calculate ratio between two metrics (relative intensity)."""
    if val1 == 0 and val2 == 0: return 1.0
    return round(min(val1, val2) / max(val1, val2), 2) if max(val1, val2) > 0 else 0.0