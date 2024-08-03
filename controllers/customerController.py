from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService
from marshmallow import ValidationError
from caching import cache
from services.customerService import get_total_order_value_per_customer
from utils.util import token_required, role_required

def save():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    customer_save = customerService.save(customer_data)
    if customer_save is not None:
        return customer_schema.jsonify(customer_save), 201
    else:
        return jsonify({"message": "Fallback method error activated", "body":customer_data}), 400

@cache.cached(timeout=60)
@token_required #added for access control
@role_required('admin')
def find_all():
    customers = customerService.find_all()
    return customers_schema.jsonify(customers), 200

def find_customer_gmail():
    customers = customerService.find_customer_gmail()
    return customers_schema.jsonify(customers), 200

# added for customer pagination
def find_all_pagination():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    return customers_schema.jsonify(customerService.find_all_pagination(page=page, per_page=per_page)), 200

# added for task 3: determine customer lifetime value
def total_order_value():
    customer_order_values = get_total_order_value_per_customer()
    return jsonify([{'id': c.id, 'name': c.name, 'total_order_value': c.total_order_value} for c in customer_order_values])

# update customer for miniproject
def update_customer(customer_id):
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    updated_customer = customerService.update(customer_id, customer_data)
    if updated_customer:
        return customer_schema.jsonify(updated_customer), 200
    else:
        return jsonify({"message": "Customer not found"}), 404

# delete customer for miniproject
def delete_customer(customer_id):
    success = customerService.delete(customer_id)
    if success:
        return jsonify({"message": "Customer deleted successfully"}), 200
    else:
        return jsonify({"message": "Customer not found"}), 404