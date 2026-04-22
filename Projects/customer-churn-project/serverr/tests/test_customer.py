# server/tests/test_customer.py
import unittest
from server.app import app  

class CustomerAPITestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_all_customers(self):
        response = self.app.get("/customers")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()