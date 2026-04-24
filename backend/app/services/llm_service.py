import openai
import json
from ..core.config import settings
from typing import Dict, Any, List

def generate_comparison_prompt(crisis_a: str, crisis_b: str, metrics: Dict[str, Any]) -> str:
    """Generate a structured prompt for the LLM narrator."""
    return f"""
    You are the Crisis Cartographer Narrator. Your role is to provide a deterministic, data-driven comparison between:
    - Crisis A: {crisis_a}
    - Crisis B: {crisis_b}

    Use the following calculated metrics to derive your insights. DO NOT hallucinate dates or numbers not provided.
    
    METRICS:
    - Tag Similarity (Jaccard): {metrics['tag_similarity']}
    - Timeline Overlap: {metrics['timeline_overlap']}
    - Casualty Intensity Ratio: {metrics['casualty_ratio']}
    - Displacement Intensity Ratio: {metrics['displacement_ratio']}
    - Duration Delta: {metrics['duration_delta_years']} years

    TASK:
    1. Identify 2-3 key similarities based STRICTLY on the metrics and cause tags.
    2. Identify 2-3 key differences based STRICTLY on the metrics.
    3. Provide a 2-sentence 'Contextual Significance' statement.
    4. List 1-2 'Data Limitations' (e.g., if Jaccard similarity is low or data confidence was low).

    OUTPUT FORMAT: JSON
    {{
        "key_similarities": ["..."],
        "key_differences": ["..."],
        "contextual_significance": "...",
        "data_limitations": ["..."]
    }}
    """

async def generate_comparison_insights(crisis_a: str, crisis_b: str, metrics: Dict[str, Any]) -> Dict[str, Any]:
    """Generate narrative insights using either OpenAI or a deterministic mock."""
    
    if settings.mock_llm:
        return generate_mock_insights(crisis_a, crisis_b, metrics)

    try:
        client = openai.OpenAI(api_key=settings.openai_api_key)
        prompt = generate_comparison_prompt(crisis_a, crisis_b, metrics)
        
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[{"role": "system", "content": "You are a professional geopolitical analyst."},
                      {"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        # Fallback to mock on any error
        return generate_mock_insights(crisis_a, crisis_b, metrics)

def generate_mock_insights(crisis_a: str, crisis_b: str, metrics: Dict[str, Any]) -> Dict[str, Any]:
    """Deterministic fallback/mock implementation."""
    similarities = []
    differences = []
    
    if metrics['tag_similarity'] > 0.5:
        similarities.append(f"Both {crisis_a} and {crisis_b} share significant structural drivers.")
    if metrics['timeline_overlap'] > 0.4:
        similarities.append("These crises occurred within a similar global geopolitical window.")
        
    if metrics['duration_delta_years'] > 5:
        differences.append(f"Significant divergence in duration ({metrics['duration_delta_years']} year gap).")
    if metrics['casualty_ratio'] < 0.4:
        differences.append("Major difference in lethality and direct casualty intensity.")
        
    return {
        "key_similarities": similarities if similarities else ["No strong structural similarities identified."],
        "key_differences": differences if differences else ["No major scale divergences identified."],
        "contextual_significance": f"Comparing {crisis_a} and {crisis_b} highlights the evolution of { 'sectarian' if metrics['tag_similarity'] > 0.3 else 'geopolitical' } conflicts.",
        "data_limitations": ["Insights are generated using deterministic fallback rules due to limited data variance."]
    }