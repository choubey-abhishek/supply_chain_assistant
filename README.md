# AI-Powered-Supply-Chain-Assistant




┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   Streamlit     │────▶│   LangChain      │────▶│   OpenAI API    │
│   Frontend      │◀────│   Agent / Chain  │     │   (LLM)         │
└─────────────────┘     └────────┬─────────┘     └─────────────────┘
                                  │
                        ┌─────────▼─────────┐
                        │   Tools / Actions │
                        └─────────┬─────────┘
                                  │
            ┌─────────────────────┼─────────────────────┐
            │                     │                     │
┌───────────▼──────────┐ ┌────────▼────────┐ ┌─────────▼─────────┐
│  Vector Store        │ │  Calculator      │ │  Mock API /       │
│  (RAG retrieval)     │ │  (EOQ, ROP, etc.)│ │  Database         │
└──────────────────────┘ └─────────────────┘ └───────────────────┘


supply-chain-assistant/
├── .env (local ke liye, GitHub pe mat dal)
├── .gitignore
├── runtime.txt
├── requirements.txt
├── config.py
├── app.py
├── README.md
├── data/
│   └── inventory.csv
└── src/
    ├── __init__.py
    ├── agent/
    │   ├── __init__.py
    │   ├── agent.py
    │   └── tools.py
    ├── rag/
    │   ├── __init__.py
    │   ├── document_loader.py
    │   ├── embeddings.py
    │   └── vector_store.py
    ├── api/
    │   ├── __init__.py
    │   └── mock_api.py
    └── utils/
        ├── __init__.py
        └── calculations.py
