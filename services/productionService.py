from sqlalchemy.orm import Session
from database import db
from models.production import Production
from models.product import Product
from sqlalchemy import func


def save(production_data):
    with Session(db.engine) as session:
        new_production = Production(product_id=production_data['product_id'], quantity_produced=production_data['quantity_produced'], date_produced=production_data['date_produced'])
        session.add(new_production)
        session.commit()
    session.refresh(new_production)
    return new_production
    

def find_all():
    query = db.select(Production)
    productions = db.session.execute(query).scalars().all()
    return productions

# added for Task 4: Evaluate Production Efficiency
def get_total_quantity_produced_on_date(specific_date):
    total_quantities = (
        db.session.query(
            Product.id,
            Product.name,
            func.sum(Production.quantity).label('total_quantity_produced')
        )
        .join(Production, Product.id == Production.product_id)  # Joining Product and Production tables
        .filter(Production.production_date == specific_date)  # Filtering by the specific date
        .group_by(Product.id, Product.name)  # Grouping by Product ID and Name
        .all()  # Fetching all results
    )
    return total_quantities