def calculate_similarity(metrics1: dict, metrics2: dict) -> float:
    # Simple similarity calculation
    common_keys = set(metrics1.keys()) & set(metrics2.keys())
    if not common_keys:
        return 0.0
    
    similarities = []
    for key in common_keys:
        if isinstance(metrics1[key], (int, float)) and isinstance(metrics2[key], (int, float)):
            diff = abs(metrics1[key] - metrics2[key])
            max_val = max(abs(metrics1[key]), abs(metrics2[key]))
            sim = 1 - (diff / max_val) if max_val > 0 else 1
            similarities.append(sim)
    
    return sum(similarities) / len(similarities) if similarities else 0.0