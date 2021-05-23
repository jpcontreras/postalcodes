from pydantic import BaseModel

class PostalCodeRequestModel(BaseModel):
    latitude: float
    longitude: float
    postal_details: list = []