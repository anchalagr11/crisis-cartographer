from typing import List, Dict, Any
from .normalization import normalize_metrics
from ..models.crisis import Crisis, CrisisStatus


def forecast_trajectory(crisis: Crisis) -> Dict[str, Any]:
    """Phase 1: Probabilistic trajectory forecast based on historical intensity."""
    norm = normalize_metrics(crisis)

    # Base rates
    cas_per_month = norm["casualties_per_year"] / 12
    disp_per_month = norm["displacement_per_year"] / 12

    # Status multipliers
    multipliers = {
        CrisisStatus.ACTIVE: 1.2,  # Escalating trend
        CrisisStatus.ESCALATING: 1.5,  # High growth
        CrisisStatus.RESOLVED: 0.1,  # Sharp decline
        CrisisStatus.FROZEN: 0.5,  # Slow stagnation
    }

    mult = multipliers.get(crisis.status, 1.0)

    forecast_12m = {
        "casualties": round(cas_per_month * 12 * mult),
        "displacement": round(disp_per_month * 12 * mult),
        "trend": "escalating" if mult > 1 else "decline" if mult < 1 else "stable",
        "confidence_score": 0.65 if crisis.status == CrisisStatus.ACTIVE else 0.8,
        "risk_factors": [],
    }

    # Add simple risk factors
    if crisis.status == CrisisStatus.ESCALATING:
        forecast_12m["risk_factors"].append(
            "High probability of regional spillover based on intensity growth."
        )
    if (
        not crisis.international_response
        or not crisis.international_response.un_involved
    ):
        forecast_12m["risk_factors"].append(
            "Lack of international mediation increases long-term volatility."
        )

    return forecast_12m


def run_scenario_analysis(crisis: Crisis, variables: Dict[str, Any]) -> Dict[str, Any]:
    """What-if analysis: How would metrics change if certain variables shifted?"""
    # Example: If international intervention increases
    base_forecast = forecast_trajectory(crisis)

    if variables.get("increase_un_involvement"):
        base_forecast["casualties"] = round(base_forecast["casualties"] * 0.7)
        base_forecast["trend"] = "stabilizing"

    return base_forecast
