import unittest

from fastapi.testclient import TestClient
from requests.auth import HTTPBasicAuth

from main import app

client = TestClient(app)


class HerokuSetupTest(unittest.TestCase):
    def setUp(self):
        self._response = client.get("/start")

    def test_correct_age_200(self):
        response = client.post(
            "/check", auth=HTTPBasicAuth(username="tester", password="1990-01-01")
        )
        self.assertEqual(response.status_code, 200)

    def test_incorrect_age_401(self):
        response = client.post(
            "/check", auth=HTTPBasicAuth(username="tester", password="2022-01-01")
        )
        self.assertEqual(response.status_code, 401)

    def test_correct_age_correct_message(self):
        response = client.post(
            "/check", auth=HTTPBasicAuth(username="tester", password="2000-01-01")
        )
        self.assertIn(
            "text/html",
            response.headers["Content-Type"],
        )
        self.assertIn(
            "<h1>Welcome tester! You are 22</h1>",
            response.content.decode(),
        )


if __name__ == "__main__":
    unittest.main()
