def plan_maintenance(state: dict) -> dict:
    """
    Agent 4: Maintenance Planning Agent
    Purpose: Generate repair plans.
    Inputs: Crack type, Defect
    Output: maintenance_action
    """
    crack_type = state.get("crack_type", "").lower()
    defect = state.get("defect", "").lower()
    
    # Example rules from user spec
    if "spalling" in defect:
        action = "Concrete Patching"
    elif "longitudinal" in crack_type:
        action = "Crack Sealing"
    elif "corrosion" in defect:
        action = "Steel Reinforcement"
    elif "transverse" in crack_type or "delamination" in defect:
        action = "Concrete Reinforcement"
    else:
        action = "Routine Inspection"
        
    return {
        "maintenance_action": action
    }
