"""
Product tests
"""
import json
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_201_CREATED


class CreateVehicleTestCase(APITestCase):
    """
    Test for create vehicle endpoint
    """

    def test_create_test_images(self):
        """
        Test for creating a vehicle with images.
        """
        data = {
            "name": "Hilux Conquest",
            "type": "Pickups",
            "model": "Conquest",
            "brand": "Toyota",
            "date": "2023-06-12",
            "price": 19000000,
            "images": [
                {
                    "url": "https://test/images/fake/1.png",
                    "title": "image title 1",
                    "detail": "image detail 1"
                },
                {
                    "url": "https://test/images/fake/2.png",
                    "title": "image title 2",
                    "detail": "image detail 2"
                }
            ]
        }
        response = self.client.post(
            "/vehicle/create", json.dumps(data, indent=4), content_type='application/json')
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_create_test_features(self):
        """
        Test for creating a vehicle with features.
        """
        data = {
            "name": "Hilux Conquest",
            "type": "Pickups",
            "model": "Conquest",
            "brand": "Toyota",
            "date": "2023-06-12",
            "price": 19000000,
            "features": [
                ["seguridad",
                    "7 airbags: frontales (conductor y acompañante), de rodilla (conductor), laterales (x2) y de cortina (x2)"],
                ["confort", "Audio con pantalla táctil de 8“ y Control de velocidad crucero"],
                ["exterior", "Faros delanteros halógenos con regulación en altura y Sistema 'Follow me home'"],
                ["transmision",
                    "Manual de 6 velocidades. Traccion 4x2"]
            ]
        }
        response = self.client.post(
            "/vehicle/create", json.dumps(data, indent=4), content_type='application/json')
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_create_test_complete(self):
        """
        Test for creating a vehicle with images and features.
        """
        data = {
            "name": "Hilux Conquest",
            "type": "Pickups",
            "model": "Conquest",
            "brand": "Toyota",
            "date": "2023-06-12",
            "price": 19000000,
            "features": [
                ["seguridad",
                    "7 airbags: frontales (conductor y acompañante), de rodilla (conductor), laterales (x2) y de cortina (x2)"],
                ["confort", "Audio con pantalla táctil de 8“ y Control de velocidad crucero"],
                ["exterior", "Faros delanteros halógenos con regulación en altura y Sistema 'Follow me home'"],
                ["transmision",
                    "Manual de 6 velocidades. Traccion 4x2"]
            ],
            "images": [
                {
                    "url": "https://test/images/fake/1.png",
                    "title": "image title 1",
                    "detail": "image detail 1"
                },
                {
                    "url": "https://test/images/fake/1.png",
                    "title": "image title 2",
                    "detail": "image detail 2"
                }
            ]
        }
        response = self.client.post(
            "/vehicle/create", json.dumps(data, indent=4), content_type='application/json')
        self.assertEqual(response.status_code, HTTP_201_CREATED)
