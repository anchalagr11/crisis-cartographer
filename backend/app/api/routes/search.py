from fastapi import APIRouter, HTTPException
from ...models.api_models import SearchQuery
from ...services import search_service
from ...models.crisis import Crisis
from typing import List

router = APIRouter()


@router.post("/search", response_model=List[Crisis])
async def search_crises(query: SearchQuery):
    try:
        return search_service.search_crises(query.query, query.filters)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
