import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy import Integer, String, Date, Float, inspect
from datetime import datetime
from datacls import Order_Dataclass, Item_Dataclass, Good_Dataclass
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

    def object_as_dict(obj):
        return {c.key: getattr(obj, c.key)
                for c in inspect(obj).mapper.column_attrs}


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


class GoodItem(Base):
    __tablename__ = 'good'
    good_id = sa.Column(Integer, primary_key=True)
    name = sa.Column(String, nullable=False)
    category = sa.Column(String, default='99')
    availqty = sa.Column(Integer, default=0)
    status = sa.Column(Integer, nullable=False)

    def __init__(self, name: str, category: str, availqty: int, status: str):
        self.name = name
        self.category = category
        self.availqty = availqty
        self.status = status


class OrderRepository():
    def map_rep_dataclass(rep_data) -> Order_Dataclass:
        order_dataclass = Order_Dataclass(
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
            order_dataclass.items.insert(i, (Item_Dataclass(
                order_id=rep_data.items[i].order_id,
                item_no=rep_data.items[i].item_no,
                good_id=rep_data.items[i].good_id,
                good_name=rep_data.items[i].good_name,
                quantity=rep_data.items[i].quantity)))
        return order_dataclass

    def read_one(self, order_id: int) -> Order_Dataclass:

        curr_session = Session()
        data = curr_session.query(OrderHeader).get(order_id)
        order_dataclass = OrderRepository.map_rep_dataclass(data)
        curr_session.close()
        return order_dataclass

    def delete_one(self, order_id: int) -> Order_Dataclass:

        curr_session = Session()
        order_data = curr_session.query(OrderHeader).get(order_id)
        order_data.status = 10
        curr_session.add(order_data)
        curr_session.commit()
        order_dataclass = OrderRepository.map_rep_dataclass(order_data)
        curr_session.close()
        return order_dataclass

    def update_one(self,
                   order_data: Order_Dataclass) -> Order_Dataclass:

        curr_session = Session()
        order_dict = asdict(order_data)
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
        order_dataclass = OrderRepository.map_rep_dataclass(rep_data=data)
        curr_session.close()
        return order_dataclass

    def create_one(self, order_data: Order_Dataclass) -> Order_Dataclass:

        curr_session = Session()
        order_dict = asdict(order_data)
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
        order_dataclass = OrderRepository.map_rep_dataclass(rep_data=data)
        curr_session.close()
        return order_dataclass


class GoodRepository():
    def map_rep_dataclass(rep_data) -> Good_Dataclass:
        good_dataclass = Good_Dataclass(
            good_id=rep_data.good_id,
            name=rep_data.name,
            category=rep_data.category,
            availqty=rep_data.availqty,
            status=rep_data.status)

        return good_dataclass

    def read_one(self, good_id: int) -> Good_Dataclass:
        curr_session = Session()
        data = curr_session.query(GoodItem).get(good_id)
        good_dataclass = GoodRepository.map_rep_dataclass(data)
        curr_session.close()
        return good_dataclass

    def delete_one(self, good_id: int) -> Good_Dataclass:

        curr_session = Session()
        orig_data = curr_session.query(GoodItem).get(good_id)
        orig_data.status = 10
        curr_session.add(orig_data)
        curr_session.commit()
        good_dataclass = GoodRepository.map_rep_dataclass(orig_data)
        curr_session.close()
        return good_dataclass

    def create_one(self, good_data: Good_Dataclass) -> Good_Dataclass:
        curr_session = Session()
        created_good = GoodItem(name=good_data.name,
                                category=good_data.category,
                                availqty=good_data.availqty,
                                status=good_data.status)
        curr_session.add(created_good)
        curr_session.commit()
        good_dataclass = GoodRepository.map_rep_dataclass(created_good)

        curr_session.close()

        return good_dataclass

    def update_one(self,
                   good_data: Good_Dataclass) -> Good_Dataclass:
        curr_session = Session()
        updated_good = GoodItem(name=good_data.name,
                                category=good_data.category,
                                availqty=good_data.availqty,
                                status=good_data.status)
        updated_good.good_id = good_data.good_id
        curr_session.merge(updated_good)
        curr_session.commit()

        data = curr_session.query(GoodItem).get(good_data.good_id)
        good_dataclass = GoodRepository.map_rep_dataclass(data)
        curr_session.close()
        return good_dataclass