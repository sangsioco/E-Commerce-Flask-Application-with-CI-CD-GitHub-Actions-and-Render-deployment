import pytest
from unittest.mock import MagicMock, patch
from faker import Faker
from werkzeug.security import generate_password_hash
from services.customerAccountService import login_customer
from app import create_app

@pytest.fixture
def app():
    # Create and configure the app instance
    app = create_app()
    return app

@pytest.fixture
def client(app):
    # Create a test client for the app
    return app.test_client()

@pytest.fixture
def faker():
    # Create a Faker instance
    return Faker()

@pytest.fixture
def mock_user(faker):
    # Create a mocked user object
    mock_user = MagicMock()
    mock_user.id = 1
    mock_user.roles = [MagicMock(role_name='admin'), MagicMock(role_name='user')]
    password = faker.password()
    mock_user.username = faker.user_name()
    mock_user.password = generate_password_hash(password)
    return mock_user, password

@pytest.fixture
def mock_db_session(mock_user):
    # Mock the db.session.execute method
    with patch('services.customerAccountService.db.session.execute') as mock_execute:
        mock_execute.return_value.scalar_one_or_none.return_value = mock_user
        yield mock_execute

@pytest.fixture
def mock_customer_query():
    # Mock the app.models.Customer.query.all method
    with patch('app.models.Customer.query.all') as mock_query_all:
        yield mock_query_all

def test_login_customer(mock_db_session, mock_user, faker):
    response = login_customer(mock_user.username, faker.password())
    assert response['status'] == 'success'

def test_get_customers(client, mock_customer_query):
    mock_customer_query.return_value = [MagicMock(id=1, name='Alice Smith')]
    response = client.get('/api/customers')
    assert response.status_code == 200
    assert 'Alice Smith' in response.data.decode()

def test_create_customer(client):
    response = client.post('/api/customers', json={'name': 'Alice Smith'})
    assert response.status_code == 201

def test_update_customer(client):
    response = client.put('/api/customers/1', json={'name': 'Alice Johnson'})
    assert response.status_code == 200
