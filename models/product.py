from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from models.orderProduct import order_product
from typing import List

class Product(Base):
    __tablename__ = 'Products'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    price: Mapped[float] = mapped_column(db.Float, nullable=False)

    orders: Mapped[List["Order"]] = db.relationship("Order", secondary=order_product, back_populates="products")
    productions: Mapped[list["Production"]] = db.relationship("Production", back_populates="product")
