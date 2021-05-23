from domain.postal_code import PostalCode

class CreatePostalCode:

    def __init__(self, latitude, longitude, postal_details):
        self.latitude       = latitude
        self.longitude      = longitude
        self.postal_details = postal_details

    def run(self):
        postal_code = PostalCode.create(
            latitude=self.latitude,
            longitude=self.longitude,
            postal_details=self.postal_details
        )
        if postal_code:
            self.postal_code = postal_code
        else:
            raise RuntimeError('Fail to create postal code')