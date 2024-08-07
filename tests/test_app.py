import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask
from services.customerAccountService import login_customer

class TestLogInCustomer(unittest.TestCase):

    @patch('services.customerAccountService.db.session.execute')
    def test_login_customer(self, mock_execute):
        faker = Faker()
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.roles = [MagicMock(role_name='admin'), MagicMock(role_name='user')]
        password = faker.password()
        mock_user.username = faker.user_name()
        mock_user.password = generate_password_hash(password)
        mock_execute.return_value.scalar_one_or_none.return_value = mock_user
        
        response = login_customer(mock_user.username, password)

        self.assertEqual(response['status'], 'success')
        self.assertTrue(check_password_hash(mock_user.password, password))

    @patch('app.models.Customer.query.all')
    def test_get_customers(self, mock_query_all):
        class MockCustomer:
            def __init__(self, id, name):
                self.id = id
                self.name = name

        mock_query_all.return_value = [MockCustomer(1, 'Alice Smith')]
        
        app = Flask(__name__)
        with app.test_client() as client:
            response = client.get('/api/customers')
            self.assertEqual(response.status_code, 200)
            self.assertIn('Alice Smith', response.data.decode())

    def test_create_customer(self):
        app = Flask(__name__)
        with app.test_client() as client:
            response = client.post('/api/customers', json={'name': 'Alice Smith'})
            self.assertEqual(response.status_code, 201)

    def test_update_customer(self):
        app = Flask(__name__)
        with app.test_client() as client:
            response = client.put('/api/customers/1', json={'name': 'Alice Johnson'})
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
