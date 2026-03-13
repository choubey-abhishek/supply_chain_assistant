from fastapi import APIRouter
from pydantic import BaseModel
from app.services.openai_service import ask_ai

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(req: ChatRequest):

    response = ask_ai(req.message)

    return {"response": response}
