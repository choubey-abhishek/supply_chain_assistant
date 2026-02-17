import math
from typing import List

def eoq(annual_demand: float, ordering_cost: float, holding_cost_per_unit: float) -> float:
    """Economic Order Quantity"""
    if holding_cost_per_unit <= 0:
        return 0.0
    return math.sqrt((2 * annual_demand * ordering_cost) / holding_cost_per_unit)

def reorder_point(lead_time_demand: float, safety_stock: float = 0) -> float:
    """Reorder point = lead time demand + safety stock"""
    return lead_time_demand + safety_stock

def simple_moving_average(demand_history: List[float], window: int = 3) -> float:
    """Forecast next period using simple moving average"""
    if len(demand_history) < window:
        return sum(demand_history) / len(demand_history)
    return sum(demand_history[-window:]) / window
