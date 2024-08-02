import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from werkzeug.security import generate_password_hash
from services.customerAccountService import login_customer

class TestLogInCustomer(unittest.TestCase):

    @patch('services.customerAccountServices.db.session.execute')
    def test_login_customer(self, mock_customer):
        faker = Faker()
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.roles = [MagicMock(role_names='admin'), MagicMock(role_name='user')]
        password = faker.password()
        mock_user.username = faker.user_name()
        mock_user.password = generate_password_hash(password)
        mock_customer.return_value.scalar_one_or_none.return_value = mock_user
        
        response = login_customer(mock_user.username, password)

        self.assertEqual(response['status'], 'success')

    @patch('app.models.Customer.query.all')
    def test_get_customers(self, mock_query_all):
        mock_query_all.return_value = [MockCustomer(1, 'Alice Smith')]
        response = self.app.get('/api/customers')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Alice Smith', response.data.decode())

    def test_create_customer(self):
        response = self.app.post('/api/customers', json={'name': 'Alice Smith'})
        self.assertEqual(response.status_code, 201)

    def test_update_customer(self):
        response = self.app.put('/api/customers/1', json={'name': 'Alice Johnson'})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()