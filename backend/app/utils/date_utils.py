from datetime import datetime


def parse_date(date_str: str) -> datetime:
    return datetime.fromisoformat(date_str)


def format_date(date: datetime) -> str:
    return date.isoformat()
