from flask import Flask
from database import db
from schema import ma
from limiter import limiter
from caching import cache
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash
from flask_cors import CORS

from models.customer import Customer
from models.customerAccount import CustomerAccount
from models.order import Order
from models.product import Product
from models.orderProduct import order_product
from models.employee import Employee
from models.production import Production
from models.role import Role
from models.customerManagementRole import CustomerManagementRole


from routes.customerBP import customer_blueprint
from routes.productBP import product_blueprint
from routes.orderBP import order_blueprint
from routes.employeeBP import employee_blueprint
from routes.productionBP import production_blueprint
from routes.customerAccountBP import customer_account_blueprint


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)
    CORS(app)

    return app

def blue_print_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(order_blueprint, url_prefix='/orders')
    app.register_blueprint(employee_blueprint, url_prefix='/employees')
    app.register_blueprint(production_blueprint, url_prefix='/productions')
    app.register_blueprint(customer_account_blueprint, url_prefix='/accounts')


def configure_rate_limit():
    limiter.limit("5 per day")(customer_blueprint)

# adding from filtering video in lesson 2
def init_customers_info_data():
    with Session(db.engine) as session:
        with session.begin():
            customers = [
                Customer(name="Customer One", email="customer1@example.com", phone="092319283"),
                Customer(name="Customer Two", email="customer2@example.com", phone="092319283"),
                Customer(name="Customer Three", email="customer3@example.com", phone="092319283")
            ]

            customerAccounts = [
                CustomerAccount(username="ctm1", password=generate_password_hash("password1"), customer_id=1),
                CustomerAccount(username="ctm2", password=generate_password_hash("password2"), customer_id=2),
                CustomerAccount(username="ctm3", password=generate_password_hash("password3"), customer_id=3)
            ]
            session.add_all(customers)
            session.add_all(customerAccounts)

# adding for role management
def init_roles_data():
    with Session(db.engine) as session:
        with session.begin():
            roles = [                
                Role(role_name='admin'),
                Role(role_name='user'),
                Role(role_name='guest')
            ]
            
            session.add_all(roles)

def init_roles_customers_data():
    with Session(db.engine) as session:
        with session.begin():
            roles_customers = [
                CustomerManagementRole(customer_management_id=1, role_id=1),
                CustomerManagementRole(customer_management_id=2, role_id=2),
                CustomerManagementRole(customer_management_id=3, role_id=3),
            ]
            session.add_all(roles_customers)
if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blue_print_config(app)
    configure_rate_limit()

    with app.app_context():
        db.drop_all()
        db.create_all()
        init_roles_data()
        init_customers_info_data()
        init_roles_customers_data()

    app.run(debug=True)