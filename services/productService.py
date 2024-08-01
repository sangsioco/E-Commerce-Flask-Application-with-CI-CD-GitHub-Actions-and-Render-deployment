from models.product import Product
from database import db
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from models.orderProduct import order_product

def save(product_data):
    with Session(db.engine) as session:
        with session.begin():
            new_product = Product(name=product_data['name'], price=product_data['price'])
            session.add(new_product)
            session.commit()
        session.refresh(new_product)
        return new_product
    
# added for products pagination
def find_all_pagination(page=1, per_page=10):
    products = db.paginate(select(Product), page=page, per_page=per_page)
    return products

# added for m13l2 objective 2 Task 2: Identify Top Selling Products
def get_top_selling_products():
    top_selling_products = (
        db.session.query(
            Product.id,
            Product.name,
            func.sum(order_product.c.quantity).label('total_quantity')
        )
        .join(order_product, Product.id == order_product.c.product_id)
        .group_by(Product.id, Product.name)
        .order_by(func.sum(order_product.c.quantity).desc())
        .all()
    )
    return top_selling_products