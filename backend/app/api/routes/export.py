import json
from fastapi import APIRouter, HTTPException
from ...models.comparison import ComparisonResult
from ...services.export_service import generate_report_json
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/export/json")
async def export_json(result: ComparisonResult):
    """Export comparison result as a structured JSON report."""
    try:
        report_content = generate_report_json(result)
        return JSONResponse(
            content=json.loads(report_content),
            headers={"Content-Disposition": "attachment; filename=crisis_report.json"},
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
