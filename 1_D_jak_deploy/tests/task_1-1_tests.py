import unittest

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class BaseUnitTests(unittest.TestCase):

    def test_status_code(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = client.get("/")
        self.assertEqual(
            response.json(),
            {"start": "1970-01-01"},
        )


if __name__ == "__main__":
    unittest.main()