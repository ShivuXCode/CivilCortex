import joblib
import pandas as pd
from pathlib import Path

# Get the project root
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "risk_model.pkl"

# Load model
model = joblib.load(MODEL_PATH)


def predict_risk(data: dict):

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    if prediction < 40:
        level = "Low"

    elif prediction < 70:
        level = "Medium"

    else:
        level = "High"

    return {
        "risk_score": round(float(prediction), 2),
        "risk_level": level
    }