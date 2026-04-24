def validate_crisis_id(crisis_id: str) -> bool:
    return isinstance(crisis_id, str) and len(crisis_id) > 0


def validate_date_range(start: str, end: str) -> bool:
    from .date_utils import parse_date

    try:
        start_date = parse_date(start)
        end_date = parse_date(end)
        return start_date <= end_date
    except:
        return False
