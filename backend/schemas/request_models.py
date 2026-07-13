from pydantic import BaseModel, Field

class MaintenanceRequest(BaseModel):
    crack_type: str = Field(default="Structural", description="Type of crack observed")
    severity: str = Field(default="medium", description="Severity level: low, medium, high")
    helmet_compliance: float = Field(default=100.0, description="Percentage of helmet compliance")
    delay_risk: str = Field(default="low", description="Risk of project delay: low, medium, high")
