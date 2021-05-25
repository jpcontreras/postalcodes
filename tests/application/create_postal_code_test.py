import unittest
from application.create_postal_code import CreatePostalCode

class CreatePostalCodeTest(unittest.TestCase):

    def test_pass(self):
        latitude = 53.5351312861402
        longitude = -2.49690382054704
        postal_details = {
            "postcode": "M46 9WU",
            "quality": 1,
            "eastings": 367163,
            "northings": 404390,
            "country": "England",
            "nhs_ha": "North West",
            "longitude": -2.496903,
            "latitude": 53.535127,
            "european_electoral_region": "North West",
            "primary_care_trust": "Ashton, Leigh and Wigan",
            "region": "North West",
            "lsoa": "Wigan 017C",
            "msoa": "Wigan 017",
            "incode": "9WU",
            "outcode": "M46",
            "parliamentary_constituency": "Bolton West",
            "admin_district": "Wigan",
            "parish": "Wigan, unparished area",
            "admin_county": "",
            "admin_ward": "Atherton",
            "ced": "",
            "ccg": "NHS Wigan Borough",
            "nuts": "Greater Manchester North West",
            "codes": {
                "admin_district": "E08000010",
                "admin_county": "E99999999",
                "admin_ward": "E05000845",
                "parish": "E43000164",
                "parliamentary_constituency": "E14000580",
                "ccg": "E38000205",
                "ccg_id": "02H",
                "ced": "E99999999",
                "nuts": "UKD36",
                "lsoa": "E01006241",
                "msoa": "E02001303",
                "lau2": "E05000845"
            },
            "distance": 0.4801241
        }
        interactor = CreatePostalCode(latitude, longitude, postal_details)
        interactor.run()

        self.assertEqual(interactor.postal_code.latitude, latitude)
        self.assertEqual(interactor.postal_code.longitude, longitude)
        self.assertEqual(interactor.postal_code.postal_details, postal_details)

    def test_fails(self):
        latitude = '53.5351312861402'
        longitude = -2.49690382054704
        postal_details = {
            "postcode": "M46 9WU",
            "quality": 1,
            "eastings": 367163,
            "northings": 404390,
            "country": "England",
            "nhs_ha": "North West",
            "longitude": -2.496903,
            "latitude": 53.535127,
            "european_electoral_region": "North West",
            "primary_care_trust": "Ashton, Leigh and Wigan",
            "region": "North West",
            "lsoa": "Wigan 017C",
            "msoa": "Wigan 017",
            "incode": "9WU",
            "outcode": "M46",
            "parliamentary_constituency": "Bolton West",
            "admin_district": "Wigan",
            "parish": "Wigan, unparished area",
            "admin_county": "",
            "admin_ward": "Atherton",
            "ced": "",
            "ccg": "NHS Wigan Borough",
            "nuts": "Greater Manchester North West",
            "codes": {
                "admin_district": "E08000010",
                "admin_county": "E99999999",
                "admin_ward": "E05000845",
                "parish": "E43000164",
                "parliamentary_constituency": "E14000580",
                "ccg": "E38000205",
                "ccg_id": "02H",
                "ced": "E99999999",
                "nuts": "UKD36",
                "lsoa": "E01006241",
                "msoa": "E02001303",
                "lau2": "E05000845"
            },
            "distance": 0.4801241
        }
        interactor = CreatePostalCode(latitude, longitude, postal_details)
        self.assertFalse(interactor.run())