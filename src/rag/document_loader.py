from langchain.schema import Document
import pandas as pd
from typing import List

def load_inventory_documents(csv_path: str) -> List[Document]:
    df = pd.read_csv(csv_path)
    documents = []
    for _, row in df.iterrows():
        # Create a descriptive text for each item
        content = (
            f"Item {row['item_id']}: {row['name']} - Category: {row['category']}. "
            f"Quantity: {row['quantity']} units, Reorder Level: {row['reorder_level']}, "
            f"Unit Price: ${row['unit_price']}, Supplier: {row['supplier']}, "
            f"Lead Time: {row['lead_time_days']} days, Annual Demand: {row['annual_demand']}, "
            f"Ordering Cost: ${row['ordering_cost']}, Holding Cost per Unit: ${row['holding_cost_per_unit']}."
        )
        metadata = {
            "item_id": row["item_id"],
            "name": row["name"],
            "category": row["category"],
            "quantity": row["quantity"],
            "reorder_level": row["reorder_level"],
            "supplier": row["supplier"],
        }
        documents.append(Document(page_content=content, metadata=metadata))
    return documents
