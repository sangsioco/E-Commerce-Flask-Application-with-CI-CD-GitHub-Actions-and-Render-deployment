import pytest
from unittest.mock import MagicMock
from faker import Faker
from werkzeug.security import generate_password_hash, check_password_hash


@pytest.fixture
def faker_instance():
    return Faker()

@pytest.fixture
def mock_user(faker_instance):
    mock_user = MagicMock()
    mock_user.id = 1
    mock_user.roles = [MagicMock(role_name='admin'), MagicMock(role_name='user')]
    password = faker_instance.password()
    mock_user.username = faker_instance.user_name()
    mock_user.password = generate_password_hash(password)
    return mock_user, password

def test_mock_user_creation(mock_user):
    user, password = mock_user
    assert user.id == 1
    assert len(user.roles) == 2
    assert user.roles[0].role_name == 'admin'
    assert user.roles[1].role_name == 'user'
    assert check_password_hash(user.password, password)
    
def test_mock_user_username(mock_user, faker_instance):
    user, _ = mock_user
    assert user.username is not None
    assert isinstance(user.username, str)

if __name__ == '__main__':
    pytest.main([__file__])
