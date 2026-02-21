import os
from dotenv import load_dotenv

# Load environment variables from .env file (local development ke liye)
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMBEDDING_MODEL = "text-embedding-ada-002"
LLM_MODEL = "gpt-4-turbo-preview"  # ya "gpt-3.5-turbo" (sasta option)

# Paths
VECTOR_STORE_PATH = "data/faiss_index"
INVENTORY_CSV_PATH = "data/inventory.csv"

# Mock API (ab use nahi hoga kyunki humne mock data tool mein daal diya)
MOCK_API_BASE_URL = "http://localhost:8000"  # optional ab
