from typing import TypedDict, Optional, List

class AgentState(TypedDict, total=False):
    # Inputs
    crack_type: str
    severity: str
    helmet_compliance: float
    delay_risk: str
    
    # Agent Outputs
    health_score: Optional[int]
    condition: Optional[str]
    risk_score: Optional[float]
    risk_level: Optional[str]
    priority: Optional[str]
    days: Optional[int]
    maintenance_action: Optional[str]
    required_workers: Optional[int]
    required_materials: Optional[List[str]]
    estimated_cost: Optional[str]
    rag_context: Optional[str]
    recommendation: Optional[str]
