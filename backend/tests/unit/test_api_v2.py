import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_get_schema():
    response = client.get("/api/v1/schema")
    assert response.status_code == 200
    data = response.json()
    assert "title" in data
    assert data["title"] == "Crisis"
    assert "properties" in data
    assert "crisis_id" in data["properties"]

def test_search_api():
    payload = {
        "query": "Syria",
        "filters": {"status": "active"}
    }
    response = client.post("/api/v1/search", json=payload)
    assert response.status_code == 200
    results = response.json()
    assert len(results) >= 1
    assert results[0]["crisis_id"] == "syria-2011"
