from fastapi import APIRouter, HTTPException
from ...models import comparison
from ...services import comparison_engine

router = APIRouter()

@router.post("/compare")
async def compare_crises(request: comparison.ComparisonRequest):
    try:
        result = await comparison_engine.compare_crises(request.crisis_ids)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))