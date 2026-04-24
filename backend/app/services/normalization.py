from datetime import datetime
from typing import Optional, Tuple
from ..models.crisis import Crisis

def normalize_date(date_str: str) -> datetime:
    """Normalize various date formats to datetime object."""
    formats = ["%Y-%m-%d", "%Y-%m", "%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Unsupported date format: {date_str}")

def calculate_duration(start: str, end: Optional[str]) -> float:
    """Calculate duration in years."""
    start_dt = normalize_date(start)
    end_dt = normalize_date(end) if end else datetime.now()
    diff = end_dt - start_dt
    return round(diff.days / 365.25, 2)

def normalize_metrics(crisis: Crisis) -> dict:
    """Standardize metrics for comparison."""
    # Ensure duration is computed
    duration = calculate_duration(crisis.start_date, crisis.end_date)
    
    # Scale casualties and displacement for relative comparison (per year of conflict)
    casualties_per_year = crisis.casualties_range.high / max(duration, 0.1)
    displacement_per_year = (crisis.displacement.idp + crisis.displacement.refugees) / max(duration, 0.1)
    
    return {
        "duration_years": duration,
        "total_casualties_est": crisis.casualties_range.high,
        "casualties_per_year": round(casualties_per_year, 2),
        "total_displacement_est": crisis.displacement.idp + crisis.displacement.refugees,
        "displacement_per_year": round(displacement_per_year, 2)
    }