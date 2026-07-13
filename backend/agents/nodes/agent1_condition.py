def assess_condition(state: dict) -> dict:
    crack_type = state.get("crack_type", "")
    severity = state.get("severity", "medium").lower()
    
    health_score = 100
    if severity == "high":
        health_score -= 50
    elif severity == "medium":
        health_score -= 25
    else:
        health_score -= 10
        
    return {
        "health_score": health_score,
        "condition": "Critical" if health_score < 60 else "Fair"
    }
