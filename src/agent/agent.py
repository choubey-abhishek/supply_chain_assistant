from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from .tools import create_rag_tool, calculator_tool, realtime_tool
from src.rag.vector_store import get_retriever
from config import LLM_MODEL, OPENAI_API_KEY

def create_supply_chain_agent():
    # Retriever for RAG
    retriever = get_retriever(k=3)
    rag_tool = create_rag_tool(retriever)
    tools = [rag_tool, calculator_tool, realtime_tool]
    
    # LLM
    llm = ChatOpenAI(model=LLM_MODEL, temperature=0, openai_api_key=OPENAI_API_KEY)
    
    # Prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", 
         "You are a helpful supply chain assistant. You have access to inventory data, "
         "can perform calculations (EOQ, reorder point, forecasts), and can fetch real-time "
         "stock information. Always check the inventory knowledge base first for any item-specific "
         "information. Use the tools as needed to answer the user accurately."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ])
    
    # Memory
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    # Agent
    agent = create_openai_tools_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True)
    
    return agent_executor
