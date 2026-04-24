from typing import List, Optional
from ..models.crisis import Crisis
from .data_loader import load_all_crises

def search_crises(query: Optional[str] = None, filters: dict = {}) -> List[Crisis]:
    all_crises = load_all_crises()
    results = []
    
    for crisis in all_crises:
        # Keyword search (name and regions)
        if query:
            q = query.lower()
            if q not in crisis.name.lower() and not any(q in r.lower() for r in crisis.regions_affected):
                continue
        
        # Tag filtering
        tags = filters.get("cause_tags", [])
        if tags and not any(tag in crisis.cause_tags for tag in tags):
            continue
            
        # Status filtering
        status = filters.get("status")
        if status and crisis.status != status:
            continue
            
        results.append(crisis)
        
    return results
