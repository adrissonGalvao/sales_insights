import unittest
import api
from flask import json


class ApiTests(unittest.TestCase):
    def setUp(self):
        self.app = api.app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status, "200 OK")
    
    def test_product_handler(self):
        response = self.app.get('/product/United Kingdom')
        self.assertEqual(response.status, "200 OK")
    
    def test_best_client(self):
        response = self.app.get('/client/')
        self.assertEqual(response.status,"200 OK")
    
    def test_price_max_and_min(self):
        response = self.app.get('/product/price/RED TOADSTOOL LED NIGHT LIGHT')
        self.assertEqual(response.status,"200 OK")
    
    def test_percentage_product(self):
        response = self.app.get('/product/percentage/RED TOADSTOOL LED NIGHT LIGHT')
        self.assertEqual(response.status,"200 OK")
if __name__ == "__main__":
    unittest.main()