def calculate_average(values: list) -> float:
    return sum(values) / len(values) if values else 0

def calculate_percentage(part: float, total: float) -> float:
    return (part / total) * 100 if total > 0 else 0