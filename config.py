import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMBEDDING_MODEL = "text-embedding-ada-002"
LLM_MODEL = "gpt-4-turbo-preview"
VECTOR_STORE_PATH = "data/faiss_index"
INVENTORY_CSV_PATH = "data/inventory.csv"
MOCK_API_BASE_URL = "http://localhost:8000"
