import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, String

Base = declarative_base()

class OrderItem(Base):
    __tablename__ = 'order_item'
    order_id = sa.Column(Integer, sa.ForeignKey("order_header.order_id"),
                         primary_key=True)
    item_no = sa.Column(Integer, autoincrement=False, primary_key=True,
                        nullable=False)
    good_id = sa.Column(Integer, sa.ForeignKey("good.good_id"))
    good_name = sa.Column(String, nullable=False)
    quantity = sa.Column(Integer, nullable=False, default=0)

    def __init__(self, order_id: int, item_no: int, good_id: int,
                 good_name: str, quantity: int):
        self.order_id = order_id
        self.item_no = item_no
        self.good_id = good_id
        self.good_name = good_name
        self.quantity = quantity