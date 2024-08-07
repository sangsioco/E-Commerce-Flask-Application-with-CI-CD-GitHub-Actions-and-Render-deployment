import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from werkzeug.security import generate_password_hash
from services.customerAccountService import login_customer

class TestLogInCustomer(unittest.TestCase):

    @patch('services.customerAccountService.db.session.execute')
    def test_login_customer(self, mock_customer):
        faker = Faker()
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.roles = [MagicMock(role_name='admin'), MagicMock(role_name='user')]
        password = faker.password()
        mock_user.username = faker.user_name()
        mock_user.password = generate_password_hash(password)
        mock_customer.return_value.scalar_one_or_none.return_value = mock_user

        # Call the login_customer function with the mock data
        result = login_customer(mock_user.username, password)

        # Perform assertions to check the result
        self.assertIsNotNone(result)
        self.assertEqual(result.id, mock_user.id)
        self.assertEqual(result.username, mock_user.username)
        self.assertTrue(result.check_password(password))

if __name__ == '__main__':
    unittest.main()
