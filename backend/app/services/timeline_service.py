from datetime import datetime
from typing import List, Dict, Any
from ..models.crisis import Crisis, KeyEvent


def calculate_relative_month(start_date_str: str, event_date_str: str) -> int:
    """Calculate the number of months between start_date and event_date."""
    # Handle potentially incomplete dates
    try:
        start_dt = datetime.strptime(start_date_str, "%Y-%m-%d")
    except ValueError:
        start_dt = (
            datetime.strptime(start_date_str, "%Y-%m")
            if len(start_date_str) == 7
            else datetime.strptime(start_date_str, "%Y")
        )

    try:
        event_dt = datetime.strptime(event_date_str, "%Y-%m-%d")
    except ValueError:
        event_dt = (
            datetime.strptime(event_date_str, "%Y-%m")
            if len(event_date_str) == 7
            else datetime.strptime(event_date_str, "%Y")
        )

    delta = (event_dt.year - start_dt.year) * 12 + (event_dt.month - start_dt.month)
    return max(0, delta)


def align_timelines(crisis: Crisis) -> List[Dict[str, Any]]:
    """Normalize crisis events to a relative timeline."""
    aligned_events = []
    for event in crisis.key_events:
        aligned_events.append(
            {
                "date": event.date,
                "relative_month": calculate_relative_month(
                    crisis.start_date, event.date
                ),
                "description": event.description,
                "type": event.type,
            }
        )
    # Sort by relative month
    return sorted(aligned_events, key=lambda x: x["relative_month"])


def group_events_by_stage(
    events: List[Dict[str, Any]],
) -> Dict[str, List[Dict[str, Any]]]:
    """Group events into logical conflict stages."""
    stages = {
        "Trigger": [],
        "Escalation": [],
        "Peak": [],
        "Negotiation": [],
        "Resolution": [],
        "Other": [],
    }

    mapping = {
        "trigger": "Trigger",
        "escalation": "Escalation",
        "peak": "Peak",
        "negotiation": "Negotiation",
        "resolution": "Resolution",
    }

    for event in events:
        stage = mapping.get(event["type"].lower(), "Other")
        stages[stage].append(event)

    return stages
