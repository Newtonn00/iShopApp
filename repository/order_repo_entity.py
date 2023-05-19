import sqlalchemy as sa
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Integer, String, Date, Float
from datetime import datetime
from order_item_repo_entity import OrderItem

Base = declarative_base()


class OrderHeader(Base):
    __tablename__ = 'order_header'
    order_id = sa.Column(Integer, primary_key=True, autoincrement=True,
                         nullable=False)
    city = sa.Column(String)
    amount = sa.Column(Float)
    vat_amount = sa.Column(Float)
    quantity = sa.Column(Integer)
    weight = sa.Column(Float)
    status = sa.Column(Integer)
    created_on = sa.Column(Date)
    created_by = sa.Column(String)
    customer_no = sa.Column(String)
    items = relationship('OrderItem')

    def __init__(self, city: str, amount: float, vat_amount: float,
                 quantity: int,
                 weight: float, status: int, created_on: datetime,
                 created_by: str, customer_no: str):
        self.city = city
        self.amount = amount
        self.vat_amount = vat_amount
        self.quantity = quantity
        self.weight = weight
        self.status = status
        self.created_on = created_on
        self.created_by = created_by
        self.customer_no = customer_no

    def __repr__(self):
        info: dict = {"order_id": self.order_id,
                      "quantity": self.quantity,
                      "status": self.status,
                      "created_on": self.created_on}
        return info