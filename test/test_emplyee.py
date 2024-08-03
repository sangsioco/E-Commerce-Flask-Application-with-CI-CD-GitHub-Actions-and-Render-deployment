import unittest
from unittest.mock import patch
from app import create_app
from models.employee import Employee


class MockEmployee:
    def __init__(self, id, name, position):
        self.id = id
        self.name = name
        self.position = position

class TestEmployeeEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.models.Employee.query.all')
    def test_get_employees(self, mock_query_all):
        # Simulate a scenario with one employee
        mock_query_all.return_value = [MockEmployee(1, 'John Doe', 'Engineer')]

        response = self.app.get('/api/employees')
        self.assertEqual(response.status_code, 200)
        self.assertIn('John Doe', response.data.decode())

    @patch('app.models.Employee.query.get')
    def test_get_employee_not_found(self, mock_query_get):
        # Simulate an employee not found scenario
        mock_query_get.return_value = None

        response = self.app.get('/api/employees/999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
