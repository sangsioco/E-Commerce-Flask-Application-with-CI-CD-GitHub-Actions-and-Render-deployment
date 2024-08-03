#added for jwt implementation
from models.schemas.customerAccountSchema import customer_accounts_schema
from services import customerAccountService
from flask import jsonify, request

def find_all():
    customer_accounts = customerAccountService.find_all()
    return customer_accounts_schema.jsonify(customer_accounts), 200

def login():
    customer = request.json
    user = customerAccountService.login_customer(customer['username'], customer['password'])
    if user:
        return jsonify(user), 200
    else:
        resp ={
            "status":"Error",
            "message":"User does not exist"
        }
        return jsonify(resp), 404
    
def create_customer_account():
    try:
        account_data = request.json
        new_account = customerAccountService.create(account_data)
        return jsonify(new_account), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400

# added for miniproject
def update_customer_account(account_id):
    try:
        account_data = request.json
        updated_account = customerAccountService.update(account_id, account_data)
        if updated_account:
            return jsonify(updated_account), 200
        else:
            return jsonify({"message": "Account not found"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 400

def delete_customer_account(account_id):
    success = customerAccountService.delete(account_id)
    if success:
        return jsonify({"message": "Account deleted successfully"}), 200
    else:
        return jsonify({"message": "Account not found"}), 404