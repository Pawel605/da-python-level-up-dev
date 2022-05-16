import datetime
import unittest

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class HerokuSetupTest(unittest.TestCase):

    def test_retrieve_is_list(self):
        create_response = client.put(
            "/events", json={"date": "2022-03-21", "event": "Pierwszy dzień wiosny"})
        self.assertEqual(create_response.status_code, 200)

        retrieve_response = client.get("/event/2022-03-21")

        self.assertEqual(retrieve_response.status_code, 200)
        response_json = retrieve_response.json()
        self.assertIsInstance(response_json, list)

    def test_retrieve_correct_dates(self):
        create_response = client.put(
            "/events", json={"date": "2022-03-22", "event": "Drugi dzień wiosny"}
        )
        self.assertEqual(create_response.status_code, 200)

        retrieve_response = client.get("/event/2022-03-22")

        self.assertEqual(retrieve_response.status_code, 200)
        response_json = retrieve_response.json()
        test_event = None
        for event in response_json:
            if event["name"] == "Drugi dzień wiosny":
                test_event = event

        self.assertIsNotNone(test_event)
        self.assertIsInstance(test_event["id"], int)
        self.assertEqual(test_event["date"], "2022-03-22")
        date_added = datetime.date.fromisoformat(test_event["date_added"])
        self.assertGreaterEqual(
            date_added, datetime.date.today() - datetime.timedelta(days=1)
        )
        self.assertLessEqual(
            date_added, datetime.date.today() + datetime.timedelta(days=1)
        )

    def test_retrieve_incorrect(self):

        retrieve_response = client.get("/event/2022-13-22")

        self.assertEqual(retrieve_response.status_code, 400)

    def test_retrieve_404(self):
        # At least one of those should be 404, unless we are really unlucky
        try_dates = ["/1994-12-29", "/1995-11-28", "/2054-01-05", "/2021-02-04"]
        response_404 = None
        for date in try_dates:
            retrieve_response = client.get("/event/" + date)
            if retrieve_response.status_code == 404:
                response_404 = retrieve_response

        self.assertEqual(response_404.status_code, 404)


if __name__ == "__main__":
    unittest.main()
