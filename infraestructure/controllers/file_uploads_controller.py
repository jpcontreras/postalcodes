import shutil
import os
from fastapi import APIRouter, File, UploadFile
from infraestructure.services.processor_service import ProcessorService

router = APIRouter()

@router.post('/file_uploads/create')
async def upload(file: UploadFile = File(...)):
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    file_path = f'./{file.filename}'
    file = open(file_path, 'rb')
    service = ProcessorService()
    service.create(file)
    os.remove(file_path)
    return {"filename": file_path}