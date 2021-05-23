from fastapi import APIRouter

router = APIRouter()

@router.post('/postal_codes/create')
async def create():
    return 'create some postal code register'