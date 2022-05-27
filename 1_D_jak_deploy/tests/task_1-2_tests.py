import unittest

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class HerokuSetupTest(unittest.TestCase):
    def test_get(self):
        response = client.get("/method")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"method": "GET"},
        )

    def test_post(self):
        response = client.post("/method")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json(),
            {"method": "POST"},
        )

    def test_put(self):
        response = client.put("/method")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"method": "PUT"},
        )

    def test_options(self):
        response = client.options("/method")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"method": "OPTIONS"},
        )

    def test_delete(self):
        response = client.delete("/method")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"method": "DELETE"},
        )


if __name__ == "__main__":
    unittest.main()