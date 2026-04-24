import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_compare_api_syria_yemen():
    payload = {"crisis_ids": ["syria-2011", "yemen-2014"]}
    response = client.post("/api/v1/compare", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["crisis_a"] == "Syrian Civil War"
    assert data["crisis_b"] == "Yemeni Civil War"
    assert "metrics" in data
    assert "tag_similarity" in data["metrics"]
    assert "duration_delta_years" in data["metrics"]
    assert len(data["key_similarities"]) > 0
