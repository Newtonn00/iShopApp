import sqlalchemy as sa
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Integer, String, Date, Float
from datetime import datetime

Base = declarative_base()


class OrderHeaderModel(Base):
    __tablename__ = 'order_header'
    order_id = sa.Column(Integer, primary_key=True, autoincrement=True,
                         nullable=False)
    city = sa.Column(String)
    amount = sa.Column(Float)
    vat_amount = sa.Column(Float)
    quantity = sa.Column(Integer)
    weight = sa.Column(Float)
    status_code = sa.Column(String)
    created_on = sa.Column(Date)
    created_by = sa.Column(String)
    customer_no = sa.Column(String)
    items = relationship("OrderItemModel")

    def __init__(self, order_id: int, city: str, amount: float, vat_amount: float,
                 quantity: int,
                 weight: float, status_code: str, created_on: datetime,
                 created_by: str, customer_no: str):
        self.order_id = order_id
        self.city = city
        self.amount = amount
        self.vat_amount = vat_amount
        self.quantity = quantity
        self.weight = weight
        self.status_code = status_code
        self.created_on = created_on
        self.created_by = created_by
        self.customer_no = customer_no

    def __repr__(self):
        info: dict = {"order_id": self.order_id,
                      "quantity": self.quantity,
                      "status_code": self.status_code,
                      "created_on": self.created_on}
        return info
class OrderItemModel(Base):
    __tablename__ = 'order_item'
    order_id = sa.Column(Integer, sa.ForeignKey("order_header.order_id"),
                         primary_key=True)
    item_no = sa.Column(Integer, autoincrement=False, primary_key=True,
                        nullable=False)
    good_id = sa.Column(Integer)
#    good_id = sa.Column(Integer, sa.ForeignKey("good.good_id"))
    good_name = sa.Column(String, nullable=False)
    quantity = sa.Column(Integer, nullable=False, default=0)

    def __init__(self, order_id: int, item_no: int, good_id: int,
                 good_name: str, quantity: int):
        self.order_id = order_id
        self.item_no = item_no
        self.good_id = good_id
        self.good_name = good_name
        self.quantity = quantity