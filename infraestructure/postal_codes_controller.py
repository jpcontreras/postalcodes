from fastapi import APIRouter
from domain.schema import PostalCodeRequestModel
from domain.postal_code import PostalCode

router = APIRouter()

@router.post('/postal_codes/create')
async def create(data: PostalCodeRequestModel):
    postal_codes = PostalCode.create(
        latitude=data.latitude,
        longitude=data.longitude,
        postal_details=data.postal_details[0]
    )
    return 'create some postal code register'