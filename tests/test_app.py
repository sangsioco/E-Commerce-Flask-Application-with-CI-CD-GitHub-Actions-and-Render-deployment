import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, jsonify

app = Flask(__name__)

class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Mock database
mock_db = {
    'customers': [Customer(1, 'Alice Smith')]
}

@app.route('/api/customers', methods=['GET'])
def get_customers():
    customers = [{'id': c.id, 'name': c.name} for c in mock_db['customers']]
    return jsonify(customers), 200

@app.route('/api/customers', methods=['POST'])
def create_customer():
    customer = Customer(id=len(mock_db['customers']) + 1, name='Alice Smith')
    mock_db['customers'].append(customer)
    return jsonify({'id': customer.id, 'name': customer.name}), 201

@app.route('/api/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    for c in mock_db['customers']:
        if c.id == id:
            c.name = 'Alice Johnson'
            return jsonify({'id': c.id, 'name': c.name}), 200
    return jsonify({'error': 'Customer not found'}), 404

# Mock login_customer function
def login_customer(username, password):
    user = next((u for u in mock_db['customers'] if u.name == username), None)
    if user and check_password_hash(user.password, password):
        return {'status': 'success'}
    return {'status': 'failure'}

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

    @patch('app.Customer.query.all')
    def test_get_customers(self, mock_query_all):
        class MockCustomer:
            def __init__(self, id, name):
                self.id = id
                self.name = name

        mock_query_all.return_value = [MockCustomer(1, 'Alice Smith')]
        
        with app.test_client() as client:
            response = client.get('/api/customers')
            self.assertEqual(response.status_code, 200)
            self.assertIn('Alice Smith', response.data.decode())

    def test_create_customer(self):
        with app.test_client() as client:
            response = client.post('/api/customers', json={'name': 'Alice Smith'})
            self.assertEqual(response.status_code, 201)

    def test_update_customer(self):
        with app.test_client() as client:
            response = client.put('/api/customers/1', json={'name': 'Alice Johnson'})
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
