from flask import jsonify, request
from models.schemas.productSchema import product_schema, products_schema
from marshmallow import ValidationError
from services.productService import get_top_selling_products
from services import productService

def save():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    try:
        product_save = productService.save(product_data)
        return product_schema.jsonify(product_save), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
# added for product pagination
def find_all_pagination():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    return products_schema.jsonify(productService.find_all_pagination(page=page, per_page=per_page)), 200

# added for m13l2 objective 2 Task 2: Identify Top Selling Products
def top_selling_products():
    products = get_top_selling_products()
    return jsonify([{'id': p.id, 'name': p.name, 'total_quantity': p.total_quantity} for p in products])