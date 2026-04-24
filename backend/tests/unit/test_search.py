import pytest
from backend.app.services import search_service

def test_search_by_query():
    # Sudan should be in results for "Sudan"
    results = search_service.search_crises(query="Sudan")
    assert len(results) >= 2  # Darfur (Sudan) and Sudan Conflict
    names = [c.name for c in results]
    assert any("Sudan" in name for name in names)

def test_search_by_tag():
    # Filter by "ethnic"
    results = search_service.search_crises(filters={"cause_tags": ["ethnic"]})
    assert len(results) > 0
    for c in results:
        assert "ethnic" in c.cause_tags

def test_search_by_status():
    results = search_service.search_crises(filters={"status": "active"})
    for c in results:
        assert c.status == "active"

def test_search_combined():
    results = search_service.search_crises(query="Ukraine", filters={"status": "active"})
    assert len(results) >= 1
    assert results[0].crisis_id == "ukraine-2022"
