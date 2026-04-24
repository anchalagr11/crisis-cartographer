import pytest
from backend.app.models.crisis import Crisis, CrisisStatus


def test_crisis_model_validation():
    valid_data = {
        "name": "Test Crisis",
        "crisis_id": "test-2024",
        "start_date": "2024-01-01",
        "end_date": None,
        "status": "active",
        "casualties_range": {"low": 1000, "high": 2000, "confidence": "medium"},
        "displacement": {"idp": 5000, "refugees": 1000, "unit": "absolute"},
        "regions_affected": ["TE"],
        "cause_tags": ["test"],
        "key_events": [
            {"date": "2024-01-01", "description": "Test onset", "type": "onset"}
        ],
        "data_sources": ["Test Source"],
        "last_updated": "2024-03-27",
    }
    crisis = Crisis(**valid_data)
    assert crisis.name == "Test Crisis"
    assert crisis.status == CrisisStatus.ACTIVE


def test_crisis_model_invalid_status():
    invalid_data = {
        "name": "Test Crisis",
        "crisis_id": "test-2024",
        "start_date": "2024-01-01",
        "status": "invalid_status",
        "casualties_range": {"low": 0, "high": 0, "confidence": "low"},
        "displacement": {"idp": 0, "refugees": 0},
        "regions_affected": [],
        "cause_tags": [],
        "key_events": [],
        "data_sources": [],
        "last_updated": "2024-03-27",
    }
    with pytest.raises(ValueError):
        Crisis(**invalid_data)
