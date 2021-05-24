from fastapi import APIRouter, File, UploadFile

router = APIRouter()

@router.post('/file_uploads/create')
async def upload(file: UploadFile = File(...)):
    #TODO: send file to process service with integration class
    return {"filename": file.filename}