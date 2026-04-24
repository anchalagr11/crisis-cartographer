import pytest
from backend.app.services import recommendation_service


def test_recommendations():
    # Test for Syria
    recs = recommendation_service.get_similar_crises("syria-2011", limit=3)
    assert len(recs) <= 3
    if recs:
        assert "similarity_score" in recs[0]
        assert "common_tags" in recs[0]
        # Syria should be similar to other sectarian/civil wars
        assert any(r["crisis_id"] == "iraq-2003" for r in recs) or any(
            r["crisis_id"] == "yemen-2014" for r in recs
        )


def test_invalid_crisis_id():
    recs = recommendation_service.get_similar_crises("non-existent")
    assert recs == []
