from fastapi import APIRouter, HTTPException
from schemas.request_models import MaintenanceRequest
from services.workflow_runner import run_analysis

router = APIRouter()

@router.post("/analyze-maintenance")
def analyze_maintenance(request: MaintenanceRequest):
    try:
        result = run_analysis(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
