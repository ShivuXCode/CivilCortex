from fastapi import FastAPI
from pydantic import BaseModel

import sys
from pathlib import Path

# Add src folder to Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR / "src"))

from predict import predict_risk

app = FastAPI(
    title="CivilCortex Agent 2 API",
    version="1.0"
)


class RiskRequest(BaseModel):

    helmet_compliance: float
    ppe_compliance: float
    equipment_condition: float
    equipment_age_years: float
    safety_delay: str
    worker_count: int
    site_type: str
    weather_condition: str
    supervisor_experience_years: float
    incident_history_count: int
    inspection_frequency_days: float
    scaffolding_used: str
    night_shift: str


@app.get("/")
def home():
    return {"message": "CivilCortex Agent 2 API Running"}


@app.post("/predict-risk")
def predict(request: RiskRequest):

    result = predict_risk(request.model_dump())

    return result