from fastapi import APIRouter

router = APIRouter()

@router.post('/file_uploads/create')
async def upload():
    return 'uploading CSV flat file'