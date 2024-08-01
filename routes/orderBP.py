from flask import Blueprint
from controllers.orderController import save, find_all_pagination, find_by_id

order_blueprint = Blueprint('order_bp', __name__)
order_blueprint.route('/', methods=['POST'])(save)
order_blueprint.route('/paginate', methods=['GET'])(find_all_pagination) #added for pagination
order_blueprint.route('/id<int:id>', methods=['GET'])(find_by_id) #added for m13l2 exercise 1 #5.