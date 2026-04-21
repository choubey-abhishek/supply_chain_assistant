Supply Chain Assistant
AI-Powered Decision Intelligence for Supply Chain Analytics

🌐 Live Application:
https://supply-chain-frontend-5p65.onrender.com/

🧠 Problem Statement

Modern supply chains generate massive amounts of operational data, but extracting actionable insights requires technical expertise.

This project solves that by enabling natural language interaction with structured data, reducing analysis time and improving decision quality.

🚀 Solution

Supply Chain Assistant is a full-stack AI application that allows users to:

Query supply chain data using plain English
Upload CSV datasets for instant analysis
Generate insights using LLM-powered reasoning
Identify inefficiencies and optimization opportunities
🏗️ System Architecture
Frontend (React)
     ↓
API Layer (Express.js)
     ↓
AI Processing (OpenAI API)
     ↓
Data Handling (CSV Parsing & Analysis)
⚙️ Key Features
💬 Conversational AI Interface
Enables natural language querying of supply chain data
📂 CSV Data Ingestion Pipeline
Parses and processes structured datasets for analysis
📊 Insight Generation Engine
Extracts patterns, trends, and anomalies
🔌 REST API Integration
Modular backend for scalable expansion
☁️ Cloud Deployment
Fully deployed on Render
📊 High-Impact Use Cases
Inventory Optimization → Reduce overstock & stockouts
Demand Forecasting Insights → Identify trends & seasonality
Bottleneck Detection → Locate inefficiencies in logistics
Data-Driven Decisions → Replace intuition with analytics
🛠️ Tech Stack
Layer	Technology
Frontend	React.js, Axios
Backend	Node.js, Express.js
AI Engine	OpenAI API
Data Layer	CSV Parsing, Data Processing
Deployment	Render
📈 Engineering Highlights
Designed a scalable API architecture separating frontend and backend concerns
Implemented asynchronous request handling for AI responses
Built a data ingestion pipeline for structured CSV analysis
Integrated LLM-based reasoning for contextual insights
Focused on extensibility for future analytics modules
🧩 Current Challenges
⚠️ Frontend rendering issue (blank screen in production)
⚠️ Latency in AI response (non-streaming responses)
🎯 Future Roadmap
🔄 Real-time streaming responses (WebSockets / SSE)
📊 Interactive dashboard with charts & KPIs
🔐 Authentication & user sessions
🗂️ File history & persistent storage
🤖 Advanced forecasting models (time-series ML)
🧪 Local Setup
# Clone repository
git clone https://github.com/choubey-abhishek/supply_chain_assistant.git

cd supply_chain_assistant

# Install dependencies
npm install

# Run backend
npm run server

# Run frontend
npm start
🤝 Contributing

Contributions are welcome!

fork → clone → create branch → commit → push → pull request
📜 License

MIT License

👨‍💻 Author
Abhishek Choubey
