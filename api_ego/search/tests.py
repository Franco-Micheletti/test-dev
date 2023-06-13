"""
Search tests
"""
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


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
        Test for type parameter = 'ALL'
        """
        response = self.client.get(
            "/search/type=ALL")
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_search_type_auto(self):
        """
        Test for type parameter = 'AUTO'
        """
        response = self.client.get(
            "/search/type=AUTO")
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_search_type_suvs(self):
        """
        Test for type parameter = 'SUVssss'
        """
        response = self.client.get(
            "/search/type=SUVssss")
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_search_invalid_type(self):
        """
        Test for type parameter = 'piCKups'
        """
        response = self.client.get(
            "/search/type=piCKups")
        self.assertEqual(response.status_code, HTTP_200_OK)
