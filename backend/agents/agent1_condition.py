def assess_condition(state: dict) -> dict:
    """
    Agent 1: Condition Assessment Agent
    Purpose: Analyze defects.
    Inputs: Crack Severity, Defect Type, Defect Count (simulated via state)
    Output: health_score, condition
    """
    severity = state.get("severity", "medium").lower()
    defect = state.get("defect", "crack").lower()
    
    # Placeholder for XGBoost model logic
    if severity == "high":
        health_score = 38
        condition = "poor"
    elif severity == "medium":
        health_score = 65
        condition = "fair"
    else:
        health_score = 90
        condition = "good"
        
    # Additional penalty for severe defects like spalling
    if defect == "spalling" and health_score > 30:
        health_score -= 10
        condition = "poor"
        
    return {
        "health_score": health_score,
        "condition": condition
    }
