from langgraph.graph import StateGraph, START, END
from agents.state import AgentState
from agents.nodes.agent1_condition import assess_condition
from agents.nodes.agent2_risk import assess_risk
from agents.nodes.agent3_priority import assess_priority
from agents.nodes.agent4_planning import plan_maintenance
from agents.nodes.agent5_resources import optimize_resources
from agents.nodes.agent6_llm import generate_recommendation

# Initialize the StateGraph with our Shared State schema
workflow = StateGraph(AgentState)

# Add all 6 agents as nodes in the graph
workflow.add_node("Agent1_Condition", assess_condition)
workflow.add_node("Agent2_Risk", assess_risk)
workflow.add_node("Agent3_Priority", assess_priority)
workflow.add_node("Agent4_Planning", plan_maintenance)
workflow.add_node("Agent5_Resources", optimize_resources)
workflow.add_node("Agent6_LLM", generate_recommendation)

# Define the flow (Edges)
workflow.add_edge(START, "Agent1_Condition")
workflow.add_edge("Agent1_Condition", "Agent2_Risk")
workflow.add_edge("Agent2_Risk", "Agent3_Priority")
workflow.add_edge("Agent3_Priority", "Agent4_Planning")
workflow.add_edge("Agent4_Planning", "Agent5_Resources")
workflow.add_edge("Agent5_Resources", "Agent6_LLM")
workflow.add_edge("Agent6_LLM", END)

# Compile the graph into a runnable application
app = workflow.compile()
