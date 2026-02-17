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
    """Fetch real-time stock and order information for a given item ID from the mock API."""
    try:
        with httpx.Client() as client:
            stock_resp = client.get(f"{MOCK_API_BASE_URL}/stock/{item_id}")
            if stock_resp.status_code != 200:
                return f"Could not fetch real-time data for {item_id}: {stock_resp.text}"
            stock_data = stock_resp.json()
            
            orders_resp = client.get(f"{MOCK_API_BASE_URL}/orders/{item_id}")
            orders_data = orders_resp.json() if orders_resp.status_code == 200 else {"recent_orders": []}
            
            return (
                f"Real-time data for {item_id}:\n"
                f"Current stock: {stock_data.get('current_stock')}\n"
                f"Pending orders: {stock_data.get('pending_orders')}\n"
                f"In transit: {stock_data.get('in_transit')}\n"
                f"Recent orders: {orders_data.get('recent_orders')}"
            )
    except Exception as e:
        return f"Error fetching real-time data: {str(e)}"
