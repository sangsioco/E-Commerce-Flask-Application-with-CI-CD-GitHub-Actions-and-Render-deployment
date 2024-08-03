from flask import jsonify, request
from models.schemas.orderSchema import order_schema, orders_schema, order_schema_customer
from marshmallow import ValidationError
from services import orderService

'''The save function is being replaced by place_order'''
#def save():
    #try:
        #order_data = order_schema.load(request.json)
    #except ValidationError as err:
        #return jsonify(err.messages), 400
    #try:
        #order_save = orderService.save(order_data)
        #return order_schema.jsonify(order_save), 201
    #except ValueError as e:
        #return jsonify({"error": str(e)}), 400

# added for miniproject
def place_order():
    try:
        order_data = order_schema.load(request.json)
        order_save = orderService.save(order_data)
        return order_schema.jsonify(order_save), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

def retrieve_order(order_id):
    order = orderService.find_by_id(order_id)
    if order:
        return order_schema_customer.jsonify(order), 200
    else:
        return jsonify({"message": "Order not found"}), 404
# added for order pagination
def find_all_pagination():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    return orders_schema.jsonify(orderService.find_all_pagination(page=page, per_page=per_page)), 200

#added for m13l2 exercise 1 #4.
def find_by_id(id):
    order = orderService.find_by_id(id)
    return order_schema_customer.jsonify(order), 200