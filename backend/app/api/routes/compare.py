from fastapi import APIRouter, HTTPException
from ...models.comparison import ComparisonRequest, ComparisonResult
from ...services import comparison_engine

router = APIRouter()

@router.post("/compare", response_model=ComparisonResult)
async def compare_crises(request: ComparisonRequest):
    try:
        return await comparison_engine.compare_crises(request.crisis_ids)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))