import unittest

from app.views import router
from fastapi.testclient import TestClient

from main import app

app.include_router(router, tags=["northwind"])
client = TestClient(app)

expected_response_suppliers_12_products = [
    {
        "ProductID": 77,
        "ProductName": "Original Frankfurter grüne Soße",
        "Category": {"CategoryID": 2, "CategoryName": "Condiments"},
        "Discontinued": 0,
    },
    {
        "ProductID": 75,
        "ProductName": "Rhönbräu Klosterbier",
        "Category": {"CategoryID": 1, "CategoryName": "Beverages"},
        "Discontinued": 0,
    },
    {
        "ProductID": 64,
        "ProductName": "Wimmers gute Semmelknödel",
        "Category": {"CategoryID": 5, "CategoryName": "Grains/Cereals"},
        "Discontinued": 0,
    },
    {
        "ProductID": 29,
        "ProductName": "Thüringer Rostbratwurst",
        "Category": {"CategoryID": 6, "CategoryName": "Meat/Poultry"},
        "Discontinued": 1,
    },
    {
        "ProductID": 28,
        "ProductName": "Rössle Sauerkraut",
        "Category": {"CategoryID": 7, "CategoryName": "Produce"},
        "Discontinued": 1,
    },
]


class BaseUnitTests(unittest.TestCase):
    def test_status_code_suppliers_12_products(self):
        response = client.get("/suppliers/12/products")
        self.assertEqual(response.status_code, 200)

    def test_response_suppliers_12_products(self):
        response = client.get("/suppliers/12/products")
        self.assertEqual(
            response.json(),
            expected_response_suppliers_12_products,
        )

    def test_not_exists_suppliers_32_products(self):
        response = client.get("/suppliers/32/products")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
