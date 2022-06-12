import unittest

from app.views import router
from fastapi.testclient import TestClient

from main import app

app.include_router(router, tags=["northwind"])
client = TestClient(app)


class BaseUnitTests(unittest.TestCase):
    def setUp(self):
        self.input_data = {
            "CompanyName": "Test Company Name",
            "ContactName": "Test Contact Name",
            "ContactTitle": "Unknown",
            "Address": "Test Address",
            "City": "Test City",
            "PostalCode": "123-123",
            "Country": "Unknown",
            "Phone": "123-123-123",
        }

    def test_create(self):

        post_response = client.post("/suppliers", json=self.input_data)
        post_response_json = post_response.json()

        self.assertIsInstance(post_response_json.get("SupplierID"), int)
        self.assertEqual(
            post_response_json.get("CompanyName"), self.input_data["CompanyName"]
        )
        self.assertEqual(
            post_response_json.get("ContactName"), self.input_data["ContactName"]
        )
        self.assertEqual(
            post_response_json.get("ContactTitle"), self.input_data["ContactTitle"]
        )
        self.assertEqual(post_response_json.get("Address"), self.input_data["Address"])
        self.assertEqual(post_response_json.get("City"), self.input_data["City"])
        self.assertEqual(
            post_response_json.get("PostalCode"), self.input_data["PostalCode"]
        )
        self.assertEqual(post_response_json.get("Country"), self.input_data["Country"])
        self.assertEqual(post_response_json.get("Phone"), self.input_data["Phone"])
        self.assertEqual(post_response_json.get("Fax"), None)
        self.assertEqual(post_response_json.get("HomePage"), None)

        get_response = client.get(f"/suppliers/{post_response_json.get('SupplierID')}")
        self.assertEqual(get_response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
