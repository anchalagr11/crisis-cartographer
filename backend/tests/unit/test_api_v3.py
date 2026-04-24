import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_compare_api_with_insights():
    payload = {"crisis_ids": ["syria-2011", "yemen-2014"]}
    response = client.post("/api/v1/compare", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "contextual_significance" in data
    assert data["contextual_significance"] is not None
    assert len(data["data_limitations"]) > 0
