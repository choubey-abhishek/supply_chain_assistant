from fastapi import APIRouter, UploadFile, File
from backend.app.services.csv_service import analyze_csv

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    result = analyze_csv(file.file)
    return {"summary": result}
