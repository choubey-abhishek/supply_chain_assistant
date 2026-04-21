# 🚛 Supply Chain Assistant

**AI-Powered Decision Intelligence for Supply Chain Analytics**

Transform raw supply chain data into actionable insights using natural language. No SQL. No spreadsheets. Just ask.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/choubey-abhishek/supply_chain_assistant/blob/main/LICENSE)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20App-brightgreen)](https://supply-chain-frontend-5p65.onrender.com/)
[![React](https://img.shields.io/badge/React-18.2+-61DAFB?logo=react)](https://react.dev)
[![Node.js](https://img.shields.io/badge/Node.js-20+-339933?logo=node.js)](https://nodejs.org)

---

### 🌐 Live Application
**Try it now:** [https://supply-chain-frontend-5p65.onrender.com/](https://supply-chain-frontend-5p65.onrender.com/)

---

### 🧠 Problem Statement
Modern supply chains generate **terabytes** of operational data every day, yet most companies still rely on spreadsheets and SQL experts to extract insights. This creates bottlenecks, delays decisions, and leaves valuable opportunities hidden in the data.

**Supply Chain Assistant** solves this by letting anyone query complex datasets using plain English.

---

### 🚀 Solution
A full-stack AI application that turns your supply chain data into intelligent conversations.

**You can:**
- Ask questions in natural language (e.g., “What are the top 5 products with highest stockout risk next month?”)
- Upload CSV files instantly for analysis
- Receive LLM-powered insights, trends, and recommendations
- Identify inefficiencies and optimization opportunities in seconds

---

### 🏗️ System Architecture

```mermaid
graph TD
    subgraph Frontend
        A[React.js UI<br/>Conversational Interface] 
    end

    subgraph Backend
        B[Express.js API Layer<br/>REST + Async Handlers]
        C[CSV Parser & Data Processor]
    end

    subgraph AI_Core
        D[OpenAI API<br/>GPT-4o Reasoning Engine]
    end

    A <--> B
    B <--> C
    B <--> D

    style A fill:#61DAFB,stroke:#222,color:#222
    style D fill:#10A37F,stroke:#222,color:#fff
