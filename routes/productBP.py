from flask import Blueprint
from controllers.productController import save, find_all_pagination, read_product, update_product, delete_product, list_all_products

product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/', methods=['POST'])(save)
product_blueprint.route('/paginate', methods=['GET'])(find_all_pagination) #added for pagination
product_blueprint.route('/top-selling-products', methods=['GET']) # added for m13l2 objective 2 Task 2: Identify Top Selling Products
product_blueprint.route('/<int:product_id>', methods=['GET'])(read_product)
product_blueprint.route('/<int:product_id>', methods=['PUT'])(update_product)
product_blueprint.route('/<int:product_id>', methods=['DELETE'])(delete_product)
product_blueprint.route('/list', methods=['GET'])(list_all_products)
