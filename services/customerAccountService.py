# added for implementing jwt m13l3
from database import db
from models.customer import Customer
from models.customerAccount import CustomerAccount
from sqlalchemy import select
from utils.util import encode_token
from werkzeug.security import check_password_hash
    
def find_all():
    query = select(CustomerAccount).join(Customer).where(Customer.id == CustomerAccount.customer_id)
    customer_accounts = db.session.execute(query).scalars().all()
    return customer_accounts

def login_customer(username, password):
    user = db.session.execute(
        db.select(CustomerAccount).where(CustomerAccount.username == username)).scalar_one_or_none()
    
    if user and check_password_hash(user.password, password):
        role_names = [role.role_name for role in user.roles]
        auth_token = encode_token(user.id, role_names)
        resp = {
            "status": "success",
            "message": "Successfully logged in",
            'auth_token': auth_token
        }
        return resp
    else:
        return None
    
# added for miniproject
def create(account_data):
    account = CustomerAccount(**account_data)
    db.session.add(account)
    db.session.commit()
    return account

def update(account_id, account_data):
    account = CustomerAccount.query.get(account_id)
    if account:
        for key, value in account_data.items():
            setattr(account, key, value)
        db.session.commit()
        return account
    return None

def delete(account_id):
    account = CustomerAccount.query.get(account_id)
    if account:
        db.session.delete(account)
        db.session.commit()
        return True
    return False