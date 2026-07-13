from agents.graph import app as workflow_app
from schemas.request_models import MaintenanceRequest

def run_analysis(request_data: MaintenanceRequest) -> dict:
    # Initialize the LangGraph state
    initial_state = {
        "crack_type": request_data.crack_type,
        "severity": request_data.severity,
        "helmet_compliance": request_data.helmet_compliance,
        "delay_risk": request_data.delay_risk
    }
    
    # Execute the compiled workflow
    final_state = workflow_app.invoke(initial_state)
    return final_state
