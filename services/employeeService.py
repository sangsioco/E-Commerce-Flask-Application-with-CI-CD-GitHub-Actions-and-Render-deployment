from sqlalchemy.orm import Session
from database import db
from models.employee import Employee
from circuitbreaker import circuit
from sqlalchemy import select, func
from models.production import Production # added for Task 1: Analyze Employee Performance

def fallback_function(employee):
    return None

@circuit(failure_threshold=1, recovery_timeout=10, fallback_function=fallback_function)
def save(employee_data):
    try:
        if employee_data['name'] == "Failure":
            raise Exception("Failure condition triggered")

        with Session(db.engine) as session:
            with session.begin():
                new_employee = Employee(name=employee_data['name'], position=employee_data['position'])
                session.add(new_employee)
                session.commit()
            session.refresh(new_employee)
            return new_employee

    except Exception as e:
        raise e

def find_all():
    query = select(Employee)
    employees = db.session.execute(query).scalars().all()
    return employees

# added for Task 1: Analyze Employee Performance
# Write a query to calculate the total quantity of products each employee has produced.

def get_total_quantity_produced_by_employee():
    results = db.session.query(
        Employee.name,
        func.sum(Production.quantity_produced).label('total_quantity_produced')
    ).join(Production, Employee.id == Production.employee_id) \
     .group_by(Employee.name) \
     .all()
    
    total_quantity_per_employee = [
        {"employee_name": name, "total_quantity_produced": total_quantity}
        for name, total_quantity in results
    ]
    
    return total_quantity_per_employee

