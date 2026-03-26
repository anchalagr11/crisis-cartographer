from .data_loader import load_crisis
from .normalization import normalize_metrics
from .similarity import calculate_similarity

async def compare_crises(crisis_ids: list) -> dict:
    crises = [load_crisis(cid) for cid in crisis_ids]
    normalized_crises = [normalize_metrics(crisis.metrics) for crisis in crises]
    
    similarities = {}
    for i in range(len(crises)):
        for j in range(i+1, len(crises)):
            sim = calculate_similarity(normalized_crises[i], normalized_crises[j])
            similarities[f"{crises[i].id}_{crises[j].id}"] = sim
    
    return {
        "similarities": similarities,
        "crises": [c.dict() for c in crises]
    }