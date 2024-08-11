import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from werkzeug.security import generate_password_hash
from services.customerAccountService import login_customer  

class TestLogInCustomer(unittest.TestCase):

    @patch('utils.util.SECRET_KEY', 'testkey')
    @patch('services.customerAccountService.db.session.execute')
    def test_login_customer(self, mock_execute):
        faker = Faker()
        password = faker.password()
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.roles = [MagicMock(role_name='admin'), MagicMock(role_name='user')]
        mock_user.username = faker.user_name()
        mock_user.password = generate_password_hash(password)

        # Ensure password is a string
        self.assertIsInstance(mock_user.password, str)

        # Print debug information for the mock user
        print("Mock User:", mock_user.username, mock_user.password)

        # Simulate the return value of the database query
        mock_execute.return_value.scalar_one_or_none.return_value = mock_user

        # Call the login_customer function with the mock data
        result = login_customer(mock_user.username, password)

        # Print debug information for the result
        print("Result:", result)

        # Perform assertions to check the result
        self.assertIsNotNone(result)
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["message"], "Successfully logged in")
        self.assertIn("auth_token", result)

//added for employee
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
