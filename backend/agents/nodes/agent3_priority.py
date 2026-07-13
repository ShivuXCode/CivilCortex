def assess_priority(state: dict) -> dict:
    risk_level = state.get("risk_level", "Low")
    delay_risk = state.get("delay_risk", "low").lower()
    
    if risk_level == "High" or delay_risk == "high":
        priority = "Immediate"
        days = 1
    elif risk_level == "Medium":
        priority = "High"
        days = 7
    else:
        priority = "Routine"
        days = 30
        
    return {
        "priority": priority,
        "days": days
    }
