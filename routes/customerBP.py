from flask import Blueprint
from controllers.customerController import save, find_all, find_customer_gmail, find_all_pagination, total_order_value, update_customer, delete_customer

customer_blueprint = Blueprint('customer_bp', __name__)
customer_blueprint.route('/', methods=['POST'])(save)
customer_blueprint.route('/', methods=['GET'])(find_all)
customer_blueprint.route('/gmail', methods=['GET'])(find_customer_gmail) #added for filtering
customer_blueprint.route('/paginate', methods=['GET'])(find_all_pagination) #added for pagination
customer_blueprint.route('/total-order-value', methods=['GET'])(total_order_value)
customer_blueprint.route('/customers/<int:customer_id>', methods=['PUT'])(update_customer)
customer_blueprint.route('/customers/<int:customer_id>', methods=['DELETE'])(delete_customer)