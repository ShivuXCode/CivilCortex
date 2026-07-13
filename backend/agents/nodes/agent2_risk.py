def assess_risk(state: dict) -> dict:
    health_score = state.get("health_score", 100)
    helmet_compliance = state.get("helmet_compliance", 100)
    
    risk_score = (100 - health_score) * 0.6 + (100 - helmet_compliance) * 0.4
    
    if risk_score > 60:
        risk_level = "High"
    elif risk_score > 30:
        risk_level = "Medium"
    else:
        risk_level = "Low"
        
    return {
        "risk_score": risk_score,
        "risk_level": risk_level
    }
