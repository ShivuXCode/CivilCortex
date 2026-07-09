from langgraph.graph import StateGraph, START, END
from .state import AgentState
from .agent1_condition import assess_condition
from .agent2_risk import assess_risk
from .agent3_priority import assess_priority
from .agent4_rag import retrieve_knowledge
from .agent5_llm import generate_recommendation

# Initialize the StateGraph with our Shared State schema
workflow = StateGraph(AgentState)

# Add all 5 agents as nodes in the graph
workflow.add_node("Agent1_Condition", assess_condition)
workflow.add_node("Agent2_Risk", assess_risk)
workflow.add_node("Agent3_Priority", assess_priority)
workflow.add_node("Agent4_RAG", retrieve_knowledge)
workflow.add_node("Agent5_LLM", generate_recommendation)

# Define the flow (Edges)
# Start -> Agent 1 & Agent 2 (They can run in sequence or parallel, here sequence for simplicity)
workflow.add_edge(START, "Agent1_Condition")
workflow.add_edge("Agent1_Condition", "Agent2_Risk")
workflow.add_edge("Agent2_Risk", "Agent3_Priority")
workflow.add_edge("Agent3_Priority", "Agent4_RAG")
workflow.add_edge("Agent4_RAG", "Agent5_LLM")
workflow.add_edge("Agent5_LLM", END)

# Compile the graph into a runnable application
app = workflow.compile()
