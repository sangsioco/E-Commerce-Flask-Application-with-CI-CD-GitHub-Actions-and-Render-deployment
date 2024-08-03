from flask import Blueprint
from controllers.orderController import find_all_pagination, find_by_id, place_order, retrieve_order

order_blueprint = Blueprint('order_bp', __name__)
order_blueprint.route('/', methods=['POST'])(place_order)
order_blueprint.route('/paginate', methods=['GET'])(find_all_pagination) #added for pagination
order_blueprint.route('/id<int:id>', methods=['GET'])(find_by_id) #added for m13l2 exercise 1 #5.
order_blueprint.route('/<int:order_id>', methods=['GET'])(retrieve_order)
