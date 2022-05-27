import random
import string
import unittest

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def make_random_string():
    return "".join(random.sample(string.ascii_lowercase, 10)) + "".join(
        str(random.randint(0, 8999))
    )


class BaseUnitTests(unittest.TestCase):
    def setUp(self):
        self.string_a = make_random_string()

    def test_get_404(self):
        response = client.get("/save" + "/" + make_random_string())
        self.assertEqual(response.status_code, 404)

    def test_put_200(self):
        response = client.put("/save" + "/" + self.string_a)
        self.assertEqual(response.status_code, 200)

    def test_put_get_redirect(self):
        response_put = client.put("/save" + "/" + self.string_a)
        self.assertEqual(response_put.status_code, 200)
        response_get = client.get("/save" + "/" + self.string_a, allow_redirects=False)
        self.assertEqual(response_get.status_code, 301)
        self.assertIn("info", response_get.headers["Location"])

    def test_put_get_redirect_delete(self):
        response_put = client.put("/save" + "/" + self.string_a)
        self.assertEqual(response_put.status_code, 200)
        response_get = client.get("/save" + "/" + self.string_a, allow_redirects=False)
        self.assertEqual(response_get.status_code, 301)
        self.assertIn("info", response_get.headers["Location"])
        response_delete = client.delete("/save" + "/" + self.string_a)
        self.assertEqual(response_delete.status_code, 200)

        response_get = client.get("/save" + "/" + self.string_a, allow_redirects=False)
        self.assertEqual(response_get.status_code, 404)


if __name__ == "__main__":
    unittest.main()
