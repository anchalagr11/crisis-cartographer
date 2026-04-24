from typing import List, Dict, Any
from .data_loader import load_all_crises
from .similarity import calculate_jaccard_similarity


def get_similar_crises(target_crisis_id: str, limit: int = 3) -> List[Dict[str, Any]]:
    """Find the most similar crises in the dataset based on cause tags and status."""
    all_crises = load_all_crises()
    target_crisis = next(
        (c for c in all_crises if c.crisis_id == target_crisis_id), None
    )

    if not target_crisis:
        return []

    recommendations = []
    for crisis in all_crises:
        if crisis.crisis_id == target_crisis_id:
            continue

        # Composite similarity score
        tag_sim = calculate_jaccard_similarity(
            target_crisis.cause_tags, crisis.cause_tags
        )
        status_match = 1.0 if target_crisis.status == crisis.status else 0.5

        score = (tag_sim * 0.7) + (status_match * 0.3)

        recommendations.append(
            {
                "crisis_id": crisis.crisis_id,
                "name": crisis.name,
                "similarity_score": round(score, 2),
                "common_tags": list(
                    set(target_crisis.cause_tags) & set(crisis.cause_tags)
                ),
            }
        )

    # Sort by score descending
    recommendations.sort(key=lambda x: x["similarity_score"], reverse=True)
    return recommendations[:limit]
