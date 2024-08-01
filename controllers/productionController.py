from flask import jsonify, request
from models.schemas.productionSchema import production_schema
from marshmallow import ValidationError
from services import productionService
from services.productionService import get_total_quantity_produced_on_date

def save():
    if request.json is None:
        return jsonify({"error": "No JSON data provided"}), 400

    try:
        production_data = production_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    try:
        production_save = productionService.save(production_data)
        return production_schema.jsonify(production_save), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

def find_all():
    production = productionService.find_all()
    return production_schema.jsonify(production), 200

# added for Task 4: Evaluate Production Efficiency
def total_quantity():
    specific_date = request.args.get('date')  # Get the date from query parameters
    if not specific_date:
        return jsonify({'error': 'Date parameter is required'}), 400
    
    try:
        total_quantities = get_total_quantity_produced_on_date(specific_date)
        return jsonify([{'id': p.id, 'name': p.name, 'total_quantity_produced': p.total_quantity_produced} for p in total_quantities])
    except Exception as e:
        return jsonify({'error': str(e)}), 500