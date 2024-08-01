from marshmallow import fields
from schema import ma

class OrderSchema(ma.Schema):
    id = fields.Integer(required=True)
    date = fields.Date(required=True)
    customer_id = fields.Integer(required=True)
    products = fields.Nested('ProductSchemaId', many=True)

#added for m13l2 exercise 1
class OrderSchemaCustomer(ma.Schema):
    id = fields.Integer(required=True)
    date = fields.Date(required=True)
    customer= fields.Nested('CustomerSchema')
    products = fields.Nested('ProductSchema', many=True)

order_schema_customer = OrderSchemaCustomer #added for m13l2 exercise 1

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)