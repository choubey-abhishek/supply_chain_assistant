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


supply_chain_assistant/
├── .env                      # API keys, environment variables
├── .gitignore
├── README.md
├── requirements.txt
├── pyproject.toml            # (optional) for dependency management
├── app/
│   ├── __init__.py
│   ├── main.py               # Streamlit entry point
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── agent.py          # LangChain agent setup
│   │   └── prompt.py         # System prompt for the agent
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── retrieval.py      # RAG retrieval tool
│   │   ├── calculator.py     # EOQ, reorder point, etc.
│   │   └── realtime.py       # Mock API client
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── indexer.py        # Load CSV/JSON, chunk, embed, store
│   │   ├── retriever.py      # Wrapper for vector store queries
│   │   └── vector_store.py   # Initialize vector DB
│   ├── data/
│   │   ├── inventory.csv     # Your dataset
│   │   └── demand_history.csv
│   ├── mock_api/
│   │   ├── __init__.py
│   │   ├── server.py         # (optional) Flask/FastAPI mock
│   │   └── data_generator.py # Generate realistic inventory data
│   └── utils/
│       ├── __init__.py
│       ├── logger.py         # Logging setup
│       └── metrics.py        # Performance evaluation helpers
└── tests/                    # Unit tests for each module
    ├── test_tools.py
    ├── test_rag.py
