class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:CIAjrj202709*!@localhost/advance_e_commerce_db'
    CACHED_TYPE = 'SimpleCache'
    DEBUG = True

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use an in-memory SQLite database
    DEBUG = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
