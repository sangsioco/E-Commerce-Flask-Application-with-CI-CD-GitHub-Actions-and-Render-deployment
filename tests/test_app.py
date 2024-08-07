import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from werkzeug.security import generate_password_hash
from services.customerAccountService import login_customer  

class TestLogInCustomer(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()
