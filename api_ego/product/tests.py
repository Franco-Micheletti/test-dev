"""
Product tests
"""
import json
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from .models import Vehicle, VehicleFeature, VehicleImage


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


class SpecificVehicleTestCase(APITestCase):
    """
    Contains the tests for specific vehicle.
    GET - PUT - DELETE
    """

    def test_get_specific_vehicle(self):
        """
        Test for fetching specific vehicle data.
        """

        # Create test object
        data = {
            "name": "get test",
            "type": "Pickups",
            "model": "Conquest",
            "brand": "Toyota",
            "date": "2023-06-23",
            "price": 500000
        }
        post_response = self.client.post(
            "/vehicle/create",
            json.dumps(data, indent=4), content_type='application/json')
        created_id = post_response.json()["vehicle"]["id"]

        # Read test object
        response = self.client.get('/specific_vehicle/id='+str(created_id))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(Vehicle.objects.get(id=created_id).name, 'get test')

    def test_update_specific_vehicle(self):
        """
        Ensure a specific_vehicle is updated correctly.
        """
        create_data = {
            "name": "Test123",
            "type": "Pickups",
            "model": "Conquest",
            "brand": "Toyota",
            "date": "2023-06-23",
            "price": 500000,
            "features": [
                ["seguridad",
                    "7 airbags: frontales (conductor y acompañante), de rodilla (conductor), laterales (x2) y de cortina (x2)"],
                ["confort", "Audio con pantalla táctil de 8“ y Control de velocidad crucero"],
                ["exterior", "Faros delanteros halógenos con regulación en altura y Sistema 'Follow me home'"],
                ["transmision", "Manual de 6 velocidades. Traccion 4x2"]
            ],
            "images": [
                {
                    "url": "https://test/images/fake/1.png",
                    "title": "image title 1 updated",
                    "detail": "image detail 1 updated"
                },
                {
                    "url": "https://test/images/fake/2.png",
                    "title": "image title 2 updated",
                    "detail": "image detail 2 updated"
                }
            ]
        }

        update_data = {
            "name": "Test123",
            "type": "Pickups",
            "model": "Conquest",
            "brand": "Toyota",
            "date": "2023-06-23",
            "price": 500000,
            "features": [
                ["seguridad",
                    "7 airbags: frontales (conductor y acompañante), de rodilla (conductor), laterales (x2) y de cortina (x2)"],
                ["confort", "Audio con pantalla táctil de 8“ y Control de velocidad crucero"]
            ],
            "images": [
                {
                    "url": "https://test/images/fake/2.png",
                    "title": "image title 2 updated",
                    "detail": "image detail 2 updated"
                }
            ]
        }

        # Create test vehicle
        response = self.client.post(
            "/vehicle/create", json.dumps(create_data, indent=4), content_type='application/json')
        created_id = response.json()["vehicle"]["id"]
        # Check if vehicle was created correctly
        self.assertEqual(VehicleFeature.objects.count(), 4)
        self.assertEqual(VehicleImage.objects.count(), 2)

        # Update test vehicle
        response = self.client.put(
            "/specific_vehicle/id="+str(created_id),
            json.dumps(update_data, indent=4), content_type='application/json')

        # Check if vehicle was updated correctly
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(Vehicle.objects.get(id=created_id).name, 'Test123')
        self.assertEqual(VehicleFeature.objects.count(), 2)
        self.assertEqual(VehicleImage.objects.count(), 1)

    def test_delete_specific_vehicle(self):
        """
        Ensure that specific vehicle is deleted correctly
        """
        # Create test object
        data = {
            "name": "Test123",
            "type": "Pickups",
            "model": "Conquest",
            "brand": "Toyota",
            "date": "2023-06-23",
            "price": 500000
        }
        response = self.client.post(
            "/vehicle/create", json.dumps(data, indent=4), content_type='application/json')
        created_id = response.json()["vehicle"]["id"]
        self.assertEqual(Vehicle.objects.count(), 1)

        # Delete test object
        response = self.client.delete("/specific_vehicle/id="+str(created_id))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(Vehicle.objects.count(), 0)
