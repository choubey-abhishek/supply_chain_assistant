import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Use stable models
LLM_MODEL = "gpt-4o-mini"
EMBEDDING_MODEL = "text-embedding-3-small"

VECTOR_STORE_PATH = "data/faiss_index"
INVENTORY_CSV_PATH = "data/inventory.csv"
MOCK_API_BASE_URL = "http://localhost:8000"
