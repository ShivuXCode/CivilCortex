def assess_risk(state: dict) -> dict:
    """
    Agent 2: Construction Risk Agent
    Purpose: Analyze site-related risks.
    Inputs: Delay Risk, PPE Compliance, Equipment Utilization
    Output: risk_score, risk_level
    """
    delay_risk = state.get("delay_risk", "low").lower()
    helmet_compliance = state.get("helmet_compliance", 100.0)
    utilization = state.get("utilization", 100.0)
    
    # Placeholder for Random Forest model logic
    risk_score = 0
    
    if delay_risk == "high":
        risk_score += 40
    elif delay_risk == "medium":
        risk_score += 20
        
    if helmet_compliance < 75:
        risk_score += 42
    elif helmet_compliance < 90:
        risk_score += 20
        
    if utilization < 50:
        risk_score += 15
        
    # Cap at 100
    risk_score = min(risk_score, 100)
    
    if risk_score > 70:
        risk_level = "high"
    elif risk_score > 40:
        risk_level = "medium"
    else:
        risk_level = "low"
        
    return {
        "risk_score": risk_score,
        "risk_level": risk_level
    }
