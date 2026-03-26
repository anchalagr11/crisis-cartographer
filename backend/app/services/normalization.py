def normalize_metrics(metrics: dict) -> dict:
    # Normalize metrics for comparison
    normalized = {}
    for key, value in metrics.items():
        if isinstance(value, (int, float)):
            # Example normalization
            normalized[key] = value / 100 if value > 100 else value
        else:
            normalized[key] = value
    return normalized