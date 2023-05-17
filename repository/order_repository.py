import sqlalchemy as sa
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Integer, String, Date, Float
from datetime import datetime
from order_entity import OrderEntity
from order_item_entity import OrderItemEntity
from repo_connection import EngineConnection

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



class OrderRepository():

    def __init__(self,engine_connection: EngineConnection,
                 order_entity: OrderEntity = None):
        self._order_entity = order_entity
        self._session = engine_connection.session
    def _map_rep_dataclass(rep_data) -> OrderEntity:
        order_dataclass = OrderEntity(
            order_id=rep_data.order_id,
            city=rep_data.city,
            amount=rep_data.amount,
            vat_amount=rep_data.vat_amount,
            quantity=rep_data.quantity,
            weight=rep_data.weight,
            status=rep_data.status,
            created_on=rep_data.created_on,
            created_by=rep_data.created_by,
            customer_no=rep_data.customer_no,
            items=[])
        for i in range(len(rep_data.items)):
            order_dataclass.items.insert(i, (OrderItemEntity(
                order_id=rep_data.items[i].order_id,
                item_no=rep_data.items[i].item_no,
                good_id=rep_data.items[i].good_id,
                good_name=rep_data.items[i].good_name,
                quantity=rep_data.items[i].quantity)))
        return order_dataclass

    def read_one(self, order_id: int) -> OrderEntity:

        curr_session = self._session()
        data = curr_session.query(OrderHeader).get(order_id)
        order_dataclass = OrderRepository._map_rep_dataclass(data)
        curr_session.close()
        return order_dataclass

    def delete_one(self, order_id: int) -> OrderEntity:

        curr_session = self._session()
        order_data = curr_session.query(OrderHeader).get(order_id)
        order_data.status = 10
        curr_session.add(order_data)
        curr_session.commit()
        order_dataclass = OrderRepository._map_rep_dataclass(order_data)
        curr_session.close()
        return order_dataclass

    def update_one(self) -> OrderEntity:

        curr_session = self._session()
        items = self._order_entity.items
        order_rec = curr_session.query(OrderHeader).get(self._order_entity.order_id)
        updated_header = OrderHeader(
                                     amount=self._order_entity.amount,
                                     vat_amount=self._order_entity.vat_amount,
                                     quantity=self._order_entity.quantity,
                                     weight=self._order_entity.weight,
                                     city=order_rec.city,
                                     status=order_rec.status,
                                     created_on=order_rec.created_on,
                                     created_by=order_rec.created_by,
                                     customer_no=order_rec.customer_no)
        updated_header.order_id = self._order_entity.order_id
        curr_session.merge(updated_header)
        for i in range(len(items)):
            updated_item = OrderItem(
                order_id=self._order_entity.order_id, item_no=(i+1)*10,
                good_id=items[i].good_id,
                good_name=items[i].good_name, quantity=items[i].quantity)
            curr_session.merge(updated_item)
        curr_session.commit()

        data = curr_session.query(OrderHeader).get(self._order_entity.order_id)
        order_dataclass = OrderRepository._map_rep_dataclass(rep_data=data)
        curr_session.close()
        return order_dataclass

    def create_one(self) -> OrderEntity:

        curr_session = self._session()
        items = self._order_entity.items
        created_header = OrderHeader(
            amount=self._order_entity.amount, vat_amount=self._order_entity.vat_amount,
            quantity=self._order_entity.quantity, weight=self._order_entity.weight,
            city=self._order_entity.city, status=1,
            created_on=datetime.now(), created_by=self._order_entity.created_by,
            customer_no=self._order_entity.customer_no)

        curr_session.add(created_header)
        curr_session.commit()
        for i in range(len(items)):
            created_item = OrderItem(
                order_id=created_header.order_id, item_no=(i + 1) * 10,
                good_id=items[i].good_id,
                good_name=items[i].good_name, quantity=items[i].quantity)
            curr_session.add(created_item)

        curr_session.commit()

        data = curr_session.query(OrderHeader).get(created_header.order_id)
        order_dataclass = OrderRepository._map_rep_dataclass(rep_data=data)
        curr_session.close()
        return order_dataclass
