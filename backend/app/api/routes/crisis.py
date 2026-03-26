from fastapi import APIRouter, HTTPException
from ...models import crisis

router = APIRouter()

@router.get("/crises")
async def get_crises():
    # Return list of crises
    pass

@router.get("/crises/{crisis_id}")
async def get_crisis(crisis_id: str):
    # Return specific crisis
    pass