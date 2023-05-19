import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, String

Base = declarative_base()

class GoodItem(Base):
    __tablename__ = 'good'
    good_id = sa.Column(Integer, primary_key=True)
    name = sa.Column(String, nullable=False)
    category = sa.Column(String, default='99')
    availqty = sa.Column(Integer, default=0)
    status = sa.Column(Integer, nullable=False)

    def __init__(self, name: str, category: str, availqty: int, status: int):
        self.name = name
        self.category = category
        self.availqty = availqty
        self.status = status