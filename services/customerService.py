from sqlalchemy.orm import Session
from database import db
from models.customer import Customer
from circuitbreaker import circuit
from sqlalchemy import select, func
from models.order import Order

def fallback_function(customer):
    return None

@circuit(failure_threshold=1, recovery_timeout=10, fallback_function=fallback_function)
def save(customer_data):
    try:
        if customer_data['name'] == "Failure":
            raise Exception("Failure condition triggered")
        
        with Session(db.engine) as session:
            with session.begin():
                new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'])
                session.add(new_customer)

                #added for ORM Transaction and Management video#29
                savepoint = session.begin_nested()
                new_nested_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'])
                session.add(new_nested_customer)

                savepoint.rollback()

            session.refresh(new_customer)
            return new_customer
    
    except Exception as e:
        raise e
    
def find_all():
    query = select(Customer)
    customers = db.session.execute(query).scalars().all()
    return customers

# added for filtering video lesson 2
def find_customer_gmail():
    query = select(Customer).where(Customer.email.like("%gmail%"))
    customers = db.session.execute(query).scallars().all()

    return customers

# added for customers pagination
def find_all_pagination(page=1, per_page=10):
    customers = db.paginate(select(Customer), page=page, per_page=per_page)
    return customers

# added for task 3: determine customer lifetime value
def get_total_order_value_per_customer(threshold):
    total_order_values = (
        db.session.query(
            Customer.id,
            Customer.name,
            func.sum(Order.total_value).label('total_order_value')
        )
        .join(Order, Customer.id == Order.customer_id)
        .group_by(Customer.id, Customer.name)
        .having(func.sum(Order.total_value) >= threshold)   # filtering threshold
        .all()
    )
    return total_order_values
