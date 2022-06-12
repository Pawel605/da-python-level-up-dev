import unittest

from fastapi.testclient import TestClient

from main import app
from app.views import router

app.include_router(router, tags=["northwind"])
client = TestClient(app)

expected_response_suppliers = [
    {"SupplierID": 1, "CompanyName": "Exotic Liquids"},
    {"SupplierID": 2, "CompanyName": "New Orleans Cajun Delights"},
    {"SupplierID": 3, "CompanyName": "Grandma Kelly's Homestead"},
    {"SupplierID": 4, "CompanyName": "Tokyo Traders"},
    {"SupplierID": 5, "CompanyName": "Cooperativa de Quesos 'Las Cabras'"},
    {"SupplierID": 6, "CompanyName": "Mayumi's"},
    {"SupplierID": 7, "CompanyName": "Pavlova, Ltd."},
    {"SupplierID": 8, "CompanyName": "Specialty Biscuits, Ltd."},
    {"SupplierID": 9, "CompanyName": "PB Knäckebröd AB"},
    {"SupplierID": 10, "CompanyName": "Refrescos Americanas LTDA"},
    {"SupplierID": 11, "CompanyName": "Heli Süßwaren GmbH & Co. KG"},
    {"SupplierID": 12, "CompanyName": "Plutzer Lebensmittelgroßmärkte AG"},
    {
        "SupplierID": 13,
        "CompanyName": "Nord-Ost-Fisch Handelsgesellschaft mbH",
    },
    {"SupplierID": 14, "CompanyName": "Formaggi Fortini s.r.l."},
    {"SupplierID": 15, "CompanyName": "Norske Meierier"},
    {"SupplierID": 16, "CompanyName": "Bigfoot Breweries"},
    {"SupplierID": 17, "CompanyName": "Svensk Sjöföda AB"},
    {"SupplierID": 18, "CompanyName": "Aux joyeux ecclésiastiques"},
    {"SupplierID": 19, "CompanyName": "New England Seafood Cannery"},
    {"SupplierID": 20, "CompanyName": "Leka Trading"},
    {"SupplierID": 21, "CompanyName": "Lyngbysild"},
    {"SupplierID": 22, "CompanyName": "Zaanse Snoepfabriek"},
    {"SupplierID": 23, "CompanyName": "Karkki Oy"},
    {"SupplierID": 24, "CompanyName": "G'day, Mate"},
    {"SupplierID": 25, "CompanyName": "Ma Maison"},
    {"SupplierID": 26, "CompanyName": "Pasta Buttini s.r.l."},
    {"SupplierID": 27, "CompanyName": "Escargots Nouveaux"},
    {"SupplierID": 28, "CompanyName": "Gai pâturage"},
    {"SupplierID": 29, "CompanyName": "Forêts d'érables"},
]


expected_response_supplier_5 = {
    "SupplierID": 5,
    "CompanyName": "Cooperativa de Quesos 'Las Cabras'",
    "ContactName": "Antonio del Valle Saavedra",
    "ContactTitle": "Export Administrator",
    "Address": "Calle del Rosal 4",
    "City": "Oviedo",
    "Region": "Asturias",
    "PostalCode": "33007",
    "Country": "Spain",
    "Phone": "(98) 598 76 54",
    "Fax": None,
    "HomePage": None,
}


class BaseUnitTests(unittest.TestCase):
    def test_status_code_suppliers(self):
        response = client.get("/suppliers")
        self.assertEqual(response.status_code, 200)

    def test_response_suppliers(self):
        response = client.get("/suppliers")
        self.assertEqual(
            response.json(),
            expected_response_suppliers,
        )

    def test_status_code_supplier_5(self):
        response = client.get("/suppliers/5")
        self.assertEqual(response.status_code, 200)

    def test_response_supplier_5(self):
        response = client.get("/suppliers/5")
        self.assertEqual(response.json(), expected_response_supplier_5)

    def test_not_exists(self):
        response = client.get("/suppliers/341")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
