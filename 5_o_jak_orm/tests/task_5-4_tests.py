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
        }
        self.update_data = {"ContactName": "Test Contact", "ContactTitle": "Test Title"}

    def test_update(self):
        post_response = client.post("/suppliers", json=self.input_data)
        post_response_json = post_response.json()
        record_id = post_response_json.get("SupplierID")
        self.assertIsInstance(record_id, int)

        put_response = client.put(f"/suppliers/{record_id}", json=self.update_data)
        put_response_json = put_response.json()
        self.assertEqual(
            put_response_json.get("CompanyName"), self.input_data["CompanyName"]
        )
        self.assertEqual(
            put_response_json.get("ContactName"), self.update_data["ContactName"]
        )
        self.assertEqual(
            put_response_json.get("ContactTitle"), self.update_data["ContactTitle"]
        )

        get_response = client.get(f"/suppliers/{record_id}")
        get_response_json = get_response.json()
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(
            get_response_json.get("CompanyName"), self.input_data["CompanyName"]
        )
        self.assertEqual(
            get_response_json.get("ContactName"), self.update_data["ContactName"]
        )
        self.assertEqual(
            get_response_json.get("ContactTitle"), self.update_data["ContactTitle"]
        )

    def test_create(self):
        put_response = client.put("/suppliers/999", json={"CompanyName": "Test Company Name"})
        self.assertEqual(put_response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
