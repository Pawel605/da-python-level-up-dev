import unittest

from fastapi.testclient import TestClient

from main import app

EDGE_UA = "Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.58 Mobile Safari/537.36 EdgA/100.0.1185.50"

client = TestClient(app)


class BaseUnitTests(unittest.TestCase):
    def test_json(self):
        response = client.get(
            "info", params={"format": "json"}, headers={"User-Agent": EDGE_UA}
        )
        self.assertEqual(response.json(), {"user_agent": EDGE_UA})

    def test_html(self):
        response = client.get(
            "info", params={"format": "html"}, headers={"User-Agent": EDGE_UA}
        )
        self.assertIn(
            f'<input type="text" id=user-agent name=agent value="{EDGE_UA}">',
            response.content.decode(),
        )

    def test_incorrect_format(self):
        response = client.get(
            "info", params={"format": "aujfdhs"}, headers={"User-Agent": EDGE_UA}
        )
        self.assertEqual(response.status_code, 400)

    def test_no_format(self):
        response = client.get("info", headers={"User-Agent": EDGE_UA})
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
