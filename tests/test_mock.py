import pytest
from unittest.mock import MagicMock
from faker import Faker
from werkzeug.security import generate_password_hash


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


if __name__ == '__main__':
    pytest.main([__file__])