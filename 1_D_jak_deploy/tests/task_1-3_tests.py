import unittest

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class HerokuSetupTest(unittest.TestCase):

    def test_monday_correct(self):
        response = client.get("/day?name=monday&number=1")
        self.assertEqual(response.status_code, 200)

    def test_tuesday_correct(self):
        response = client.get("/day?name=tuesday&number=2")
        self.assertEqual(response.status_code, 200)

    def test_saturday_correct(self):
        response = client.get("/day?name=saturday&number=6")
        self.assertEqual(response.status_code, 200)

    def test_sunday_correct(self):
        response = client.get("/day?name=sunday&number=7")
        self.assertEqual(response.status_code, 200)

    def test_nonday_404(self):
        response = client.get("/day?name=nonday&number=2")
        self.assertEqual(response.status_code, 400)

    def test_sunday_4_404(self):
        response = client.get("/day?name=sunday&number=4")
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
