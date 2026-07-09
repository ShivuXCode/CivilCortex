def assess_priority(state: dict) -> dict:
    """
    Agent 3: Maintenance Priority Agent
    Purpose: Determine urgency.
    Inputs: Condition, Risk Level
    Output: priority
    """
    condition = state.get("condition", "good").lower()
    risk_level = state.get("risk_level", "low").lower()
    
    # Logic rule matching user spec
    if condition == "poor" and risk_level == "high":
        priority = "critical"
    elif condition == "poor" or risk_level == "high":
        priority = "high"
    elif condition == "fair" and risk_level == "medium":
        priority = "medium"
    else:
        priority = "low"
        
    return {
        "priority": priority
    }
