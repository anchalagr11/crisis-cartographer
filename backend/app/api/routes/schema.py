from fastapi import APIRouter
from ...models.crisis import Crisis

router = APIRouter()

@router.get("/schema")
async def get_schema():
    return Crisis.schema()