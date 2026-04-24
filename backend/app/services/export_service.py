import json
from datetime import datetime
from typing import Dict, Any
from ..models.comparison import ComparisonResult


def generate_report_json(result: ComparisonResult) -> str:
    """Generate a structured analytical report in JSON format."""
    report = {
        "report_id": f"CC-{int(datetime.now().timestamp())}",
        "generated_at": datetime.now().isoformat(),
        "summary": {
            "subject_a": result.crisis_a,
            "subject_b": result.crisis_b,
            "context": result.contextual_significance,
        },
        "metrics": result.metrics.dict(),
        "insights": {
            "similarities": result.key_similarities,
            "differences": result.key_differences,
        },
        "forecasts": result.forecasts,
        "data_limitations": result.data_limitations,
    }
    return json.dumps(report, indent=4)


def generate_summary_text(result: ComparisonResult) -> str:
    """Generate a plain-text executive summary."""
    lines = [
        f"CRISIS CARTOGRAPHER: EXECUTIVE SUMMARY",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "=" * 40,
        f"Comparison: {result.crisis_a} vs {result.crisis_b}",
        f"Context: {result.contextual_significance}",
        "\nKEY FINDINGS:",
    ]
    for sim in result.key_similarities[:2]:
        lines.append(f"- Similarity: {sim}")
    for diff in result.key_differences[:2]:
        lines.append(f"- Difference: {diff}")

    lines.append("\nPREDICTIVE TRENDS:")
    for name, forecast in result.forecasts.items():
        lines.append(
            f"- {name}: {forecast['trend'].upper()} (Confidence: {forecast['confidence_score']*100}%)"
        )

    return "\n".join(lines)
