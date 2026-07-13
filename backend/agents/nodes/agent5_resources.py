from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from typing import List

class ResourceResponse(BaseModel):
    required_workers: int = Field(description="Estimated number of workers needed")
    required_materials: List[str] = Field(description="List of required materials")
    estimated_cost: str = Field(description="Estimated cost in USD formatted as a string, e.g., '$5000'")

def optimize_resources(state: dict) -> dict:
    action = state.get("maintenance_action", "Surface Sealing")
    
    llm = ChatGoogleGenerativeAI(model="gemini-flash-latest", temperature=0.1)
    structured_llm = llm.with_structured_output(ResourceResponse)
    
    prompt = f"To execute the civil engineering maintenance action '{action}', estimate the required number of workers, specific materials needed, and the total dollar cost based on standard industry practices."
    
    response = structured_llm.invoke(prompt)
    
    return {
        "required_workers": response.required_workers,
        "required_materials": response.required_materials,
        "estimated_cost": response.estimated_cost
    }
