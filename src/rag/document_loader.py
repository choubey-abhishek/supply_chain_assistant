from langchain.schema import Document
import csv
from typing import List

def load_inventory_documents(csv_path: str) -> List[Document]:
    documents = []
    with open(csv_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
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
                "quantity": int(row["quantity"]),
                "reorder_level": int(row["reorder_level"]),
                "supplier": row["supplier"],
            }
            documents.append(Document(page_content=content, metadata=metadata))
    return documents
