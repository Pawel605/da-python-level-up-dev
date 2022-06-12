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

    def test_delete(self):
        post_response = client.post("/suppliers", json=self.input_data)
        post_response_json = post_response.json()
        record_id = post_response_json.get("SupplierID")

        del_response = client.delete(f"/suppliers/{record_id}")
        self.assertEqual(del_response.status_code, 204)

        get_response = client.get(f"/suppliers/{record_id}")
        self.assertEqual(get_response.status_code, 404)

    def test_delete_not_exists_supplier(self):
        del_response = client.delete(f"/suppliers/998")
        self.assertEqual(del_response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
