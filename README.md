# AI-Powered Supply Chain Assistant

A RAG-based chatbot for inventory and supply chain queries with agentic workflows.

## Features
- Semantic search over inventory data
- Calculations (EOQ, reorder point, forecasting)
- Real-time mock data simulation
- Streamlit frontend

## Deployment on Render
1. Set environment variable `OPENAI_API_KEY`.
2. Build command: `pip install -r requirements.txt`
3. Start command: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
4. Add `runtime.txt` to pin Python 3.12.6.
