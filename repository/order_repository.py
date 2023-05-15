import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy import Integer, String, Date, Float, inspect
from datetime import datetime
from order_entity import OrderEntity
from order_item_entity import OrderItemEntity
from dataclasses import asdict

engine = sa.create_engine(
    "postgresql+psycopg2://ishop_admin:Password78@178.20.40.136/ishop_db",
    echo=True, pool_size=5)
engine.connect()
Session = sessionmaker(bind=engine)
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

    def __init__(self,order_entity: OrderEntity):
        self._order_entity = order_entity

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
        for i in range(rep_data.items.__len__()):
            order_dataclass.items.insert(i, (OrderItemEntity(
                order_id=rep_data.items[i].order_id,
                item_no=rep_data.items[i].item_no,
                good_id=rep_data.items[i].good_id,
                good_name=rep_data.items[i].good_name,
                quantity=rep_data.items[i].quantity)))
        return order_dataclass

    def read_one(self, order_id: int) -> OrderEntity:

        curr_session = Session()
        data = curr_session.query(OrderHeader).get(order_id)
        order_dataclass = OrderRepository._map_rep_dataclass(data)
        curr_session.close()
        return order_dataclass

    def delete_one(self, order_id: int) -> OrderEntity:

        curr_session = Session()
        order_data = curr_session.query(OrderHeader).get(order_id)
        order_data.status = 10
        curr_session.add(order_data)
        curr_session.commit()
        order_dataclass = OrderRepository._map_rep_dataclass(order_data)
        curr_session.close()
        return order_dataclass

    def update_one(self) -> OrderEntity:

        curr_session = Session()
        order_dict = asdict(self._order_entity)
        items = order_dict["items"]
        order_rec = curr_session.query(OrderHeader).get(order_dict["order_id"])

        updated_header = OrderHeader(
                                     amount=order_dict["amount"],
                                     vat_amount=order_dict["vat_amount"],
                                     quantity=order_dict["quantity"],
                                     weight=order_dict["weight"],
                                     city=order_rec.city,
                                     status=order_rec.status,
                                     created_on=order_rec.created_on,
                                     created_by=order_rec.created_by,
                                     customer_no=order_rec.customer_no)
        updated_header.order_id = order_dict["order_id"]
        curr_session.merge(updated_header)
        for i in range(len(items)):
            good = items[i]
            updated_item = OrderItem(
                order_id=order_dict["order_id"], item_no=(i+1)*10,
                good_id=good["good_id"],
                good_name=good["good_name"], quantity=good["quantity"])
            curr_session.merge(updated_item)
        curr_session.commit()

        data = curr_session.query(OrderHeader).get(order_dict["order_id"])
        order_dataclass = OrderRepository._map_rep_dataclass(rep_data=data)
        curr_session.close()
        return order_dataclass

    def create_one(self) -> OrderEntity:

        curr_session = Session()
        order_dict = asdict(self._order_entity)
        items = order_dict["items"]
        created_header = OrderHeader(
            amount=order_dict["amount"], vat_amount=order_dict["vat_amount"],
            quantity=order_dict["quantity"], weight=order_dict["weight"],
            city=order_dict["city"], status=1,
            created_on=datetime.now(), created_by=order_dict["created_by"],
            customer_no=order_dict["customer_no"])

        curr_session.add(created_header)
        curr_session.commit()
        for i in range(len(items)):
            good = order_dict["items"][i]
            created_item = OrderItem(
                order_id=created_header.order_id, item_no=(i + 1) * 10,
                good_id=good["good_id"],
                good_name=good["good_name"], quantity=good["quantity"])
            curr_session.add(created_item)

        curr_session.commit()

        data = curr_session.query(OrderHeader).get(created_header.order_id)
        order_dataclass = OrderRepository._map_rep_dataclass(rep_data=data)
        curr_session.close()
        return order_dataclass
