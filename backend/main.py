from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.agent.agent import create_supply_chain_agent

app = FastAPI(title="Supply Chain API")

# CORS allow karo (frontend ko access mile)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Production mein specific origin daal
    allow_methods=["*"],
    allow_headers=["*"],
)

# Agent globally initialize karo (singleton)
agent = create_supply_chain_agent()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        result = agent.invoke({"input": request.message})
        return ChatResponse(response=result["output"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "ok"}
