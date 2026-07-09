from typing import TypedDict, Optional

class AgentState(TypedDict):
    # Module 1 Inputs (Infrastructure Cognition)
    crack_type: str
    severity: str
    location: str
    crack_length: float
    crack_width: float

    # Module 2 Inputs (Construction Intelligence)
    helmet_compliance: float
    project_progress: float
    equipment_utilization: float
    delay_risk: str

    # Agent 1 Outputs
    health_score: Optional[int]
    condition: Optional[str]

    # Agent 2 Outputs
    risk_score: Optional[int]
    risk_level: Optional[str]

    # Agent 3 Outputs
    priority: Optional[str]
    priority_score: Optional[int]

    # Agent 4 Outputs
    retrieved_context: Optional[str]

    # Agent 5 Outputs
    maintenance_plan: Optional[str]
    estimated_cost: Optional[str]
    estimated_duration: Optional[str]
    required_workers: Optional[int]
