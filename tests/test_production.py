import unittest
from unittest.mock import patch
from app import app

class TestProductionEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.models.Production.query.all')
    def test_get_productions(self, mock_query_all):
        mock_query_all.return_value = [MockProduction(1, 1, 100, '2024-08-01')]
        response = self.app.get('/api/productions')
        self.assertEqual(response.status_code, 200)
        self.assertIn('2024-08-01', response.data.decode())

    def test_create_production(self):
        response = self.app.post('/api/productions', json={'product_id': 1, 'quantity_produced': 100, 'date_produced': '2024-08-01'})
        self.assertEqual(response.status_code, 201)

    def test_update_production(self):
        response = self.app.put('/api/productions/1', json={'quantity_produced': 120})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
