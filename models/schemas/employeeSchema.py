from marshmallow import fields
from schema import ma

class EmployeeSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    position = fields.Str(required=True)

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)
