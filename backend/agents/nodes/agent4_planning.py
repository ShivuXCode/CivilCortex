import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from pydantic import BaseModel, Field

class MaintenanceActionResponse(BaseModel):
    maintenance_action: str = Field(description="The specific engineering action required, e.g., 'Concrete Reinforcement'")

def plan_maintenance(state: dict) -> dict:
    priority = state.get("priority", "Routine")
    crack_type = state.get("crack_type", "")
    
    # 1. Retrieve RAG Context
    rag_context = "No specific regulatory guidelines found in knowledge base."
    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "chroma_db")
    
    if os.path.exists(db_path):
        try:
            embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2")
            db = Chroma(persist_directory=db_path, embedding_function=embeddings)
            
            # Query the database for standard clauses related to the defect type
            docs = db.similarity_search(crack_type, k=2)
            if docs:
                rag_context = "\n\n".join([doc.page_content for doc in docs])
        except Exception as e:
            print(f"RAG Retrieval Error: {e}")
            pass
            
    # 2. Use LLM to determine the best action, now grounded in RAG Context
    llm = ChatGoogleGenerativeAI(model="gemini-flash-latest", temperature=0.1)
    structured_llm = llm.with_structured_output(MaintenanceActionResponse)
    
    prompt = f"""
    Based on the following regulatory tunnel standards:
    {rag_context}
    
    Given a {crack_type} crack with {priority} priority, what is the single best engineering maintenance action to perform according to the standard? Respond concisely.
    """
    
    response = structured_llm.invoke(prompt)
    
    return {
        "maintenance_action": response.maintenance_action,
        "rag_context": rag_context
    }
