from fastapi import FastAPI, HTTPException
from typing import Dict, List

app = FastAPI(title="Supply Chain Mock API")

# Mock database: item_id -> current stock, pending orders
mock_db: Dict[str, Dict] = {
    "A001": {"current_stock": 145, "pending_orders": 20, "in_transit": 50},
    "A002": {"current_stock": 310, "pending_orders": 0, "in_transit": 100},
    "A003": {"current_stock": 42, "pending_orders": 15, "in_transit": 0},
    "A004": {"current_stock": 480, "pending_orders": 200, "in_transit": 500},
    "A005": {"current_stock": 220, "pending_orders": 30, "in_transit": 0},
}

@app.get("/stock/{item_id}")
async def get_stock(item_id: str):
    if item_id not in mock_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, **mock_db[item_id]}

@app.get("/orders/{item_id}")
async def get_orders(item_id: str):
    # Simulate recent orders (last 5)
    if item_id not in mock_db:
        raise HTTPException(status_code=404, detail="Item not found")
    # Mock order history
    orders = [
        {"date": "2026-02-10", "quantity": 20},
        {"date": "2026-02-05", "quantity": 15},
        {"date": "2026-01-28", "quantity": 30},
    ]
    return {"item_id": item_id, "recent_orders": orders}
