import os
import pickle
import numpy as np
from .embeddings import get_embeddings
from .document_loader import load_inventory_documents
from config import VECTOR_STORE_PATH, INVENTORY_CSV_PATH

class SimpleVectorStore:
    def __init__(self, documents=None, embeddings=None):
        self.documents = documents or []
        self.embeddings = embeddings
        self.vectors = []
        if documents and embeddings:
            self._embed_documents()
    
    def _embed_documents(self):
        texts = [doc.page_content for doc in self.documents]
        self.vectors = self.embeddings.embed_documents(texts)
        self.vectors = np.array(self.vectors)
    
    def similarity_search(self, query: str, k: int = 3):
        if not self.documents:
            return []
        query_vector = self.embeddings.embed_query(query)
        query_vector = np.array(query_vector)
        similarities = np.dot(self.vectors, query_vector) / (
            np.linalg.norm(self.vectors, axis=1) * np.linalg.norm(query_vector) + 1e-9
        )
        top_indices = np.argsort(similarities)[-k:][::-1]
        return [self.documents[i] for i in top_indices]
    
    def save_local(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as f:
            pickle.dump({
                'documents': self.documents,
                'vectors': self.vectors
            }, f)
    
    @classmethod
    def load_local(cls, path, embeddings):
        with open(path, 'rb') as f:
            data = pickle.load(f)
        store = cls(data['documents'], embeddings)
        store.vectors = data['vectors']
        return store

def create_vector_store(force_recreate=False):
    embeddings = get_embeddings()
    if os.path.exists(VECTOR_STORE_PATH) and not force_recreate:
        with open(VECTOR_STORE_PATH, 'rb') as f:
            return SimpleVectorStore.load_local(VECTOR_STORE_PATH, embeddings)
    else:
        documents = load_inventory_documents(INVENTORY_CSV_PATH)
        vector_store = SimpleVectorStore(documents, embeddings)
        vector_store.save_local(VECTOR_STORE_PATH)
        return vector_store

def get_retriever(k=3):
    vector_store = create_vector_store()
    return vector_store
