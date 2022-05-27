import datetime
import unittest

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class BaseUnitTests(unittest.TestCase):

    def test_add_correct(self):
        response = client.put("/events", json={"date": "2022-03-01", "event": "Dzień Balearów"})
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        # Not caring about those in this test
        del response_json["id"]
        del response_json["date_added"]
        self.assertEqual(
            response_json,
            {
                "name": "Dzień Balearów",
                "date": "2022-03-01",
            },
        )

    def test_add_correct_data(self):
        response = client.put(
            "/events", json={"date": "2022-03-01", "event": "Dzień Balearów"}
        )
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertIsInstance(response_json["id"], int)
        self.assertIsInstance(response_json["date_added"], str)

        date_added = datetime.date.fromisoformat(response_json["date_added"])
        self.assertGreaterEqual(
            date_added, datetime.date.today() - datetime.timedelta(days=1)
        )
        self.assertLessEqual(
            date_added, datetime.date.today() + datetime.timedelta(days=1)
        )


if __name__ == "__main__":
    unittest.main()
