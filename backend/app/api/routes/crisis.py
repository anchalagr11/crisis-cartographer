from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from ...models.crisis import Crisis
from ...services import data_loader
from ...services.recommendation_service import get_similar_crises

router = APIRouter()

@router.get("/crises", response_model=List[Crisis])
async def get_crises():
    try:
        return data_loader.load_all_crises()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading crises: {str(e)}")

@router.get("/crises/{crisis_id}")
async def get_crisis(crisis_id: str):
    try:
        crisis = data_loader.load_crisis(crisis_id)
        recommendations = get_similar_crises(crisis_id)
        
        # Return composite object
        return {
            "crisis": crisis,
            "similar_crises": recommendations
        }
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Crisis not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))