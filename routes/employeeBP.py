from flask import Blueprint
from controllers.employeeController import save, find_all
from services.employeeService import get_total_quantity_produced_by_employee

employee_blueprint = Blueprint('employee_bp', __name__)
employee_blueprint.route('/', methods=['POST'])(save)
employee_blueprint.route('/', methods=['GET'])(find_all)
employee_blueprint.route('/total-quantity-produced', methods=['GET'])(get_total_quantity_produced_by_employee)
