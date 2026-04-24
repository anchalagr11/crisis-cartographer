from .data_loader import load_crisis
from .normalization import normalize_metrics
from .similarity import (
    calculate_jaccard_similarity,
    calculate_timeline_overlap,
    calculate_metric_ratio,
)
from .llm_service import generate_comparison_insights
from .timeline_service import align_timelines
from .geo_service import calculate_geospatial_proximity, get_country_centroids
from .recommendation_service import get_similar_crises
from .prediction_service import forecast_trajectory
from ..models.comparison import ComparisonResult, ComparisonMetrics


async def compare_crises(crisis_ids: list) -> ComparisonResult:
    if len(crisis_ids) < 2:
        raise ValueError("At least two crisis IDs are required for comparison.")

    c1 = load_crisis(crisis_ids[0])
    c2 = load_crisis(crisis_ids[1])

    m1 = normalize_metrics(c1)
    m2 = normalize_metrics(c2)

    tag_sim = calculate_jaccard_similarity(c1.cause_tags, c2.cause_tags)
    time_overlap = calculate_timeline_overlap(
        c1.start_date, c1.end_date, c2.start_date, c2.end_date
    )

    cas_ratio = calculate_metric_ratio(
        m1["casualties_per_year"], m2["casualties_per_year"]
    )
    disp_ratio = calculate_metric_ratio(
        m1["displacement_per_year"], m2["displacement_per_year"]
    )
    dur_delta = abs(m1["duration_years"] - m2["duration_years"])

    geo_metrics = calculate_geospatial_proximity(
        c1.regions_affected, c2.regions_affected
    )

    metrics = {
        "tag_similarity": tag_sim,
        "timeline_overlap": time_overlap,
        "casualty_ratio": cas_ratio,
        "displacement_ratio": disp_ratio,
        "duration_delta_years": round(dur_delta, 2),
        "geospatial_metrics": geo_metrics,
    }

    comp_metrics = ComparisonMetrics(**metrics)

    # Generate narrative insights via LLM (or mock/fallback)
    insights = await generate_comparison_insights(c1.name, c2.name, metrics)

    # Align timelines
    aligned_a = align_timelines(c1)
    aligned_b = align_timelines(c2)

    return ComparisonResult(
        crisis_a=c1.name,
        crisis_b=c2.name,
        metrics=comp_metrics,
        key_similarities=insights.get("key_similarities", []),
        key_differences=insights.get("key_differences", []),
        contextual_significance=insights.get("contextual_significance"),
        data_limitations=insights.get("data_limitations", []),
        aligned_events={c1.crisis_id: aligned_a, c2.crisis_id: aligned_b},
        region_coordinates={
            c1.crisis_id: get_country_centroids(c1.regions_affected),
            c2.crisis_id: get_country_centroids(c2.regions_affected),
        },
        recommendations={
            c1.crisis_id: get_similar_crises(c1.crisis_id),
            c2.crisis_id: get_similar_crises(c2.crisis_id),
        },
        forecasts={
            c1.crisis_id: forecast_trajectory(c1),
            c2.crisis_id: forecast_trajectory(c2),
        },
    )
