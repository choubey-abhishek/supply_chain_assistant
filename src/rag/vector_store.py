import os
import pickle
from langchain.vectorstores import FAISS
from .embeddings import get_embeddings
from .document_loader import load_inventory_documents
from config import VECTOR_STORE_PATH, INVENTORY_CSV_PATH

def create_vector_store(force_recreate=False):
    embeddings = get_embeddings()
    
    if os.path.exists(VECTOR_STORE_PATH) and not force_recreate:
        vector_store = FAISS.load_local(VECTOR_STORE_PATH, embeddings)
    else:
        documents = load_inventory_documents(INVENTORY_CSV_PATH)
        vector_store = FAISS.from_documents(documents, embeddings)
        vector_store.save_local(VECTOR_STORE_PATH)
    return vector_store

def get_retriever(k=3):
    vector_store = create_vector_store()
    return vector_store.as_retriever(search_kwargs={"k": k})
