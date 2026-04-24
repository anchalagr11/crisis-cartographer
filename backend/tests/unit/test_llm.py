import pytest
from backend.app.services import llm_service


@pytest.mark.asyncio
async def test_llm_mock_insights():
    metrics = {
        "tag_similarity": 0.8,
        "timeline_overlap": 0.5,
        "casualty_ratio": 0.9,
        "displacement_ratio": 0.8,
        "duration_delta_years": 1.2,
    }
    insights = await llm_service.generate_comparison_insights(
        "Crisis A", "Crisis B", metrics
    )

    assert "key_similarities" in insights
    assert len(insights["key_similarities"]) > 0
    assert "contextual_significance" in insights
    assert "Crisis A" in insights["contextual_significance"]


def test_prompt_generation():
    metrics = {
        "tag_similarity": 0.5,
        "timeline_overlap": 0.2,
        "casualty_ratio": 0.1,
        "displacement_ratio": 0.1,
        "duration_delta_years": 10,
    }
    prompt = llm_service.generate_comparison_prompt("A", "B", metrics)
    assert "Timeline Overlap: 0.2" in prompt
    assert "Crisis A: A" in prompt
