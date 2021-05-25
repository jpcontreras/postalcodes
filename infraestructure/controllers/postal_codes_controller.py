from fastapi import APIRouter
from domain.schema import PostalCodeRequestModel
#from domain.postal_code import PostalCode
from application.create_postal_code import CreatePostalCode

router = APIRouter()

@router.post('/postal_codes/create')
async def create(data: PostalCodeRequestModel):
    interactor = CreatePostalCode(data.latitude, data.longitude, data.postal_details[0])
    interactor.run()
    return 'Postal code created.'

