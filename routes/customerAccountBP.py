# added for jwt implmentation
from flask import Blueprint
from controllers.customerAccountController import find_all, login, create_customer_account, delete_customer_account, update_customer_account

customer_account_blueprint = Blueprint('customer_account_bp', __name__)
customer_account_blueprint.route('/', methods=['GET'])(find_all)
customer_account_blueprint.route('/login', methods=['POST'])(login)
customer_account_blueprint.route('/accounts', methods=['POST'])(create_customer_account)
customer_account_blueprint.route('/accounts/<int:account_id>', methods=['PUT'])(update_customer_account)
customer_account_blueprint.route('/accounts/<int:account_id>', methods=['DELETE'])(delete_customer_account)
