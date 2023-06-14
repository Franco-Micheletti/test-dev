"""
Search tests
"""
import json
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED


class SearchWithOrderByTestCase(APITestCase):
    """
    Test for search with orderby parameters
    """

    def test_search_auto_price(self):
        """
        Test for type = 'auto' and order_by = 'price'.
        Expected response : 200 OK
        """
        response = self.client.get("/search/type=auto&order_by=price")
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_search_suvs_date(self):
        """
        Test for type = 'SUVs' and order_by = 'date'.
        Expected response : 200 OK
        """
        response = self.client.get("/search/type=suvs&order_by=date")
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_search_invalid_order_by(self):
        """
        Test for invalid order_by parameter.
        Expected response : 400 BAD REQUEST
        """
        response = self.client.get(
            "/search/type=suvs&order_by=dwdwdwdqdwdwq23232")
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_search_invalid_type(self):
        """
        Test for invalid type parameter.
        Expected response : 400 BAD REQUEST
        """
        response = self.client.get(
            "/search/type=dwdwddwdw&order_by=dwdwdwdqdwdwq23232")
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)


class SearchWithOutOrderByTestCase(APITestCase):
    """
    Tests for search endpoint without order by parameter
    """

    def test_search_type_all(self):
        """
        Test for search endpoint with type parameter = 'ALL'
        """

        # Create test object
        data = {
            "name": "search all test",
            "type": "Pickups",
            "model": "Conquest",
            "brand": "Toyota",
            "date": "2023-06-23",
            "price": 500000
        }
        post_response = self.client.post(
            "/vehicle/create",
            json.dumps(data, indent=4), content_type='application/json')

        # Check if test object was created successfully
        self.assertEqual(post_response.status_code, HTTP_201_CREATED)

        # Get test object
        response = self.client.get("/search/type=ALL")

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_type_auto(self):
        """
        Test for search endpoint with type parameter = 'AUTO'
        """
        # Create test object
        data = {
            "name": "search all test",
            "type": "Auto",
            "model": "Conquest",
            "brand": "Toyota",
            "date": "2023-06-23",
            "price": 500000
        }
        post_response = self.client.post(
            "/vehicle/create",
            json.dumps(data, indent=4), content_type='application/json')

        # Check if test object was created successfully
        self.assertEqual(post_response.status_code, HTTP_201_CREATED)

        # Get test object
        response = self.client.get("/search/type=auto")

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_type_suvs(self):
        """
        Test for search endpoint with type parameter = 'SUVssss'
        """
        # Create test object
        data = {
            "name": "search all test",
            "type": "SUVs",
            "model": "Conquest",
            "brand": "Toyota",
            "date": "2023-06-23",
            "price": 500000
        }
        post_response = self.client.post(
            "/vehicle/create",
            json.dumps(data, indent=4), content_type='application/json')

        # Check if test object was created successfully
        self.assertEqual(post_response.status_code, HTTP_201_CREATED)

        # Get test object
        response = self.client.get("/search/type=suvs")

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_type_pickup(self):
        """
        Test for search endpoint with type parameter = 'piCKups'
        """
        # Create test object
        data = {
            "name": "search all test",
            "type": "pickups",
            "model": "Conquest",
            "brand": "Toyota",
            "date": "2023-06-23",
            "price": 500000
        }
        post_response = self.client.post(
            "/vehicle/create",
            json.dumps(data, indent=4), content_type='application/json')

        # Check if test object was created successfully
        self.assertEqual(post_response.status_code, HTTP_201_CREATED)

        # Get test object
        response = self.client.get("/search/type=piCKups")

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
