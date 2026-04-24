import pytest
from backend.app.services import timeline_service


def test_calculate_relative_month():
    # Same month
    assert timeline_service.calculate_relative_month("2020-01-01", "2020-01-15") == 0
    # Next month
    assert timeline_service.calculate_relative_month("2020-01-01", "2020-02-01") == 1
    # Next year
    assert timeline_service.calculate_relative_month("2020-01-01", "2021-01-01") == 12
    # Multiple years
    assert timeline_service.calculate_relative_month("2010-01-01", "2012-03-01") == 26


def test_group_events_by_stage():
    events = [
        {"type": "trigger", "description": "Start"},
        {"type": "escalation", "description": "More fighting"},
        {"type": "other", "description": "Random thing"},
    ]
    grouped = timeline_service.group_events_by_stage(events)
    assert len(grouped["Trigger"]) == 1
    assert len(grouped["Escalation"]) == 1
    assert len(grouped["Other"]) == 1
    assert grouped["Trigger"][0]["description"] == "Start"
