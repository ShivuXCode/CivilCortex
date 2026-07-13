from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

class RecommendationResponse(BaseModel):
    recommendation: str = Field(description="A comprehensive, multi-paragraph recommendation report for stakeholders")

def generate_recommendation(state: dict) -> dict:
    # Gather state
    crack_type = state.get("crack_type", "Unknown")
    health_score = state.get("health_score", 100)
    risk_level = state.get("risk_level", "Low")
    priority = state.get("priority", "Routine")
    action = state.get("maintenance_action", "None")
    cost = state.get("estimated_cost", "$0")
    workers = state.get("required_workers", 0)
    materials = state.get("required_materials", [])
    rag_context = state.get("rag_context", "None provided.")
    
    llm = ChatGoogleGenerativeAI(model="gemini-flash-latest", temperature=0.5)
    structured_llm = llm.with_structured_output(RecommendationResponse)
    
    prompt = f"""
    Act as a Lead Civil Engineer and Standards Compliance Officer. 
    Write a comprehensive recommendation report for stakeholders based on the following automated analysis:
    - Crack Type: {crack_type}
    - Health Score (0-100): {health_score}
    - Overall Risk Level: {risk_level}
    - Priority: {priority}
    - Proposed Action: {action}
    - Estimated Cost: {cost}
    - Required Workers: {workers}
    - Materials: {', '.join(materials)}
    
    CRITICAL INSTRUCTION: You must base your recommendation strictly on the following Regulatory Tunnel Standards. 
    You MUST explicitly cite the specific clauses from these standards in your report to justify the action and materials.
    
    REGULATORY STANDARDS RETRIEVED (RAG Context):
    {rag_context}
    
    The report should clearly summarize the condition, justify the risk and priority, and outline the proposed maintenance plan and resources required.
    """
    
    response = structured_llm.invoke(prompt)
    
    return {
        "recommendation": response.recommendation
    }
