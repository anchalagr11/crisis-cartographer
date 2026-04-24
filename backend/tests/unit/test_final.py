import pytest
from backend.app.services import prediction_service, export_service
from backend.app.models.crisis import Crisis


def test_prediction_logic():
    # Mock a crisis
    crisis_data = {
        "name": "Test",
        "crisis_id": "test",
        "status": "escalating",
        "start_date": "2020-01-01",
        "regions_affected": ["SD"],
        "cause_tags": ["political"],
        "key_events": [],
        "casualties_range": {"low": 1000, "high": 2000, "confidence": "high"},
        "displacement": {"idp": 1, "refugees": 1},
        "last_updated": "2020-01-01",
        "data_sources": [],
    }
    crisis = Crisis(**crisis_data)
    forecast = prediction_service.forecast_trajectory(crisis)
    assert forecast["trend"] == "escalating"
    assert forecast["casualties"] > 0


def test_export_summary():
    # Very basic check
    from backend.app.models.comparison import ComparisonResult, ComparisonMetrics

    metrics = ComparisonMetrics(
        tag_similarity=0.5,
        timeline_overlap=0.2,
        casualty_ratio=1.0,
        displacement_ratio=1.0,
        duration_delta_years=0,
    )
    result = ComparisonResult(
        crisis_a="A", crisis_b="B", metrics=metrics, contextual_significance="Test"
    )
    summary = export_service.generate_summary_text(result)
    assert "CRISIS CARTOGRAPHER" in summary
    assert "A vs B" in summary
