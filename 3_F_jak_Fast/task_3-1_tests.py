import unittest

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class HerokuSetupTest(unittest.TestCase):
    def setUp(self):
        self._response = client.get("/start")

    def test_status_code(self):
        self.assertEqual(self._response.status_code, 200)

    def test_content_type(self):
        self.assertIn("text/html", self._response.headers["Content-Type"])

    def test_response(self):
        self.assertIn(
            "<h1>The unix epoch started at 1970-01-01</h1>",
            self._response.content.decode(),
        )


if __name__ == "__main__":
    unittest.main()
