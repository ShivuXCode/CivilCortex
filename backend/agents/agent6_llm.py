def generate_recommendation(state: dict) -> dict:
    """
    Agent 6: LLM Decision Support Agent
    Purpose: Generate engineering recommendations.
    Inputs: Health Score, Risk Level, Maintenance Action, Priority
    Output: recommendation
    """
    health_score = state.get("health_score", 100)
    risk_level = state.get("risk_level", "low").capitalize()
    action = state.get("maintenance_action", "No action").capitalize()
    days = state.get("days", 0)
    
    # Simulate LLM Response Generation based on the exact prompt example
    # "Health Score = 38, Risk Level = High, Maintenance Action = Concrete Reinforcement"
    
    if health_score < 50:
        recommendation = f"The structure exhibits severe deterioration (Health Score: {health_score}) and elevated construction risk (Risk Level: {risk_level}). Immediate {action.lower()} is recommended within {days} days to prevent further structural degradation."
    elif health_score < 80:
        recommendation = f"The structure shows moderate wear. Scheduled {action.lower()} is advised within the next {days} days to maintain safety standards."
    else:
        recommendation = "The structure is in good condition. Routine visual inspection is sufficient at this time."
        
    return {
        "recommendation": recommendation
    }
