import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from werkzeug.security import generate_password_hash, check_password_hash
from app import create_app
from config import TestConfig
from services.customerAccountService import login_customer

class TestLogInCustomer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app('TestConfig')  # Or whatever your test config is named
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()

    @classmethod
    def tearDownClass(cls):
        cls.app_context.pop()

    def setUp(self):
        self.faker = Faker()
        self.mock_user, self.password = self.create_mock_user()

    def create_mock_user(self):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.roles = [MagicMock(role_name='admin'), MagicMock(role_name='user')]
        password = self.faker.password()
        mock_user.username = self.faker.user_name()
        mock_user.password = generate_password_hash(password)
        return mock_user, password

    def test_mock_user_creation(self):
        user, password = self.mock_user, self.password
        self.assertEqual(user.id, 1)
        self.assertEqual(len(user.roles), 2)
        self.assertEqual(user.roles[0].role_name, 'admin')
        self.assertEqual(user.roles[1].role_name, 'user')
        self.assertTrue(check_password_hash(user.password, password))

    def test_mock_user_username(self):
        user, _ = self.mock_user
        self.assertIsNotNone(user.username)
        self.assertIsInstance(user.username, str)

    @patch('services.customerAccountService.db.session.execute')
    def test_login_customer(self, mock_customer):
        user, password = self.mock_user
        mock_customer.return_value.scalar_one_or_none.return_value = user
        
        response = login_customer(user.username, password)

        self.assertEqual(response['status'], 'success')

    @patch('app.models.Customer.query.all')
    def test_get_customers(self, mock_query_all):
        mock_query_all.return_value = [MagicMock(id=1, name='Alice Smith')]
        response = self.client.get('/api/customers')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Alice Smith', response.data.decode())

    def test_create_customer(self):
        response = self.client.post('/api/customers', json={'name': 'Alice Smith'})
        self.assertEqual(response.status_code, 201)

    def test_update_customer(self):
        response = self.client.put('/api/customers/1', json={'name': 'Alice Johnson'})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
