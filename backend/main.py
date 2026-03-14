from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.routers.chat import router as chat_router
from backend.app.routers.upload import router as upload_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api")
app.include_router(upload_router, prefix="/api")

@app.get("/")
def root():
    return {"status": "API running"}
