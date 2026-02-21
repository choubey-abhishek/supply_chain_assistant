from langchain.tools import BaseTool, StructuredTool, tool
from langchain.retrievers import BaseRetriever
from typing import Type, Optional, List
from pydantic import BaseModel, Field
import httpx
import json
from src.utils.calculations import eoq, reorder_point, simple_moving_average
from config import MOCK_API_BASE_URL

class RAGToolInput(BaseModel):
    query: str = Field(description="The search query to find inventory information")

def create_rag_tool(retriever: BaseRetriever):
    @tool(args_schema=RAGToolInput)
    def rag_tool(query: str) -> str:
        """Retrieve inventory information from the knowledge base using a semantic search query."""
        docs = retriever.get_relevant_documents(query)
        if not docs:
            return "No relevant inventory records found."
        # Format results
        results = []
        for doc in docs:
            results.append(doc.page_content)
        return "\n\n".join(results)
    return rag_tool

class CalculatorInput(BaseModel):
    operation: str = Field(description="Operation type: 'eoq', 'reorder_point', or 'forecast'")
    params: dict = Field(description="Parameters as JSON object")

@tool(args_schema=CalculatorInput)
def calculator_tool(operation: str, params: dict) -> str:
    """Perform supply chain calculations: EOQ, reorder point, or demand forecast."""
    try:
        if operation == "eoq":
            annual_demand = params.get("annual_demand")
            ordering_cost = params.get("ordering_cost")
            holding_cost = params.get("holding_cost_per_unit")
            if None in (annual_demand, ordering_cost, holding_cost):
                return "Missing parameters for EOQ."
            result = eoq(annual_demand, ordering_cost, holding_cost)
            return f"EOQ: {result:.2f} units"
        
        elif operation == "reorder_point":
            lead_time_demand = params.get("lead_time_demand")
            safety_stock = params.get("safety_stock", 0)
            if lead_time_demand is None:
                return "Missing lead_time_demand."
            result = reorder_point(lead_time_demand, safety_stock)
            return f"Reorder point: {result:.2f} units"
        
        elif operation == "forecast":
            demand_history = params.get("demand_history")
            window = params.get("window", 3)
            if not demand_history:
                return "Missing demand_history."
            result = simple_moving_average(demand_history, window)
            return f"Forecast for next period: {result:.2f} units"
        
        else:
            return f"Unknown operation: {operation}"
    except Exception as e:
        return f"Calculation error: {str(e)}"

class RealTimeDataInput(BaseModel):
    item_id: str = Field(description="The item ID to fetch real-time data for")

@tool(args_schema=RealTimeDataInput)
def realtime_tool(item_id: str) -> str:
    """Fetch real-time stock and order information for a given item ID using mock data."""
    # Mock data directly in the tool (no external API needed)
    mock_db = {
        "A001": {"current_stock": 145, "pending_orders": 20, "in_transit": 50},
        "A002": {"current_stock": 310, "pending_orders": 0, "in_transit": 100},
        "A003": {"current_stock": 42, "pending_orders": 15, "in_transit": 0},
        "A004": {"current_stock": 480, "pending_orders": 200, "in_transit": 500},
        "A005": {"current_stock": 220, "pending_orders": 30, "in_transit": 0},
    }
    
    mock_orders = {
        "A001": [
            {"date": "2026-02-10", "quantity": 20}, 
            {"date": "2026-02-05", "quantity": 15},
            {"date": "2026-01-28", "quantity": 30}
        ],
        "A002": [
            {"date": "2026-02-12", "quantity": 10}, 
            {"date": "2026-02-08", "quantity": 25},
            {"date": "2026-02-01", "quantity": 15}
        ],
        "A003": [
            {"date": "2026-02-09", "quantity": 5}, 
            {"date": "2026-02-03", "quantity": 8},
            {"date": "2026-01-25", "quantity": 12}
        ],
        "A004": [
            {"date": "2026-02-11", "quantity": 100}, 
            {"date": "2026-02-04", "quantity": 150},
            {"date": "2026-01-28", "quantity": 200}
        ],
        "A005": [
            {"date": "2026-02-07", "quantity": 30}, 
            {"date": "2026-02-01", "quantity": 20},
            {"date": "2026-01-24", "quantity": 25}
        ],
    }
    
    if item_id not in mock_db:
        return f"Item {item_id} not found in inventory."
    
    stock = mock_db[item_id]
    orders = mock_orders.get(item_id, [])
    
    return (
        f"📦 **Real-time data for {item_id}**\n\n"
        f"**Current stock:** {stock['current_stock']} units\n"
        f"**Pending orders:** {stock['pending_orders']} units\n"
        f"**In transit:** {stock['in_transit']} units\n"
        f"**Recent orders:** {orders}"
    )
