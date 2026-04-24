from pydantic import BaseModel


class SearchQuery(BaseModel):
    query: str
    filters: dict = {}
