from fastapi import APIRouter, UploadFile, File
from app.services.csv_service import analyze_csv

router = APIRouter()

@router.post("/upload")
async def upload_csv(file: UploadFile = File(...)):

    result = analyze_csv(file.file)

    return {"summary": result}
