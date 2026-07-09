def optimize_resources(state: dict) -> dict:
    """
    Agent 5: Resource Optimization Agent
    Purpose: Estimate resources.
    Inputs: Maintenance Type, Priority, Severity
    Output: cost, workers, days
    """
    action = state.get("maintenance_action", "").lower()
    priority = state.get("priority", "low").lower()
    
    # Base values
    cost = 50000
    workers = 2
    days = 2
    
    # Adjust based on action
    if "reinforcement" in action:
        cost = 250000
        workers = 8
        days = 15
    elif "patching" in action:
        cost = 80000
        workers = 4
        days = 5
    elif "sealing" in action:
        cost = 30000
        workers = 2
        days = 3
        
    # Adjust based on priority multiplier
    if priority == "critical":
        cost = int(cost * 1.5) # Overtime/rush fees
        workers += 2
        days = max(1, days - 2) # Faster completion
        
    return {
        "cost": cost,
        "workers": workers,
        "days": days
    }
