from datetime import datetime
from typing import List

from src.entity.order_entity import OrderEntity
from src.entity.order_item_entity import OrderItemEntity
from repo_connection import EngineConnection
from src.repository.order_repo_entity import OrderHeaderModel, OrderItemModel



class OrderRepository:

    def __init__(self, engine_connection: EngineConnection):
        self._session = engine_connection.session

    def get_order_count(self,customerno: str) -> int:
        curr_session = self._session()
        orders_count = curr_session.query(OrderHeaderModel).filter(OrderHeaderModel.customer_no==customerno).count()
        curr_session.close()
        return orders_count

    def _map_rep_dataclass(rep_data) -> OrderEntity:
        order_dataclass = OrderEntity(
            order_id=rep_data.order_id,
            city=rep_data.city,
            amount=rep_data.amount,
            vat_amount=rep_data.vat_amount,
            quantity=rep_data.quantity,
            weight=rep_data.weight,
            status_code=rep_data.status_code.rstrip(),
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

    def read_one(self, order_id: int) -> List[OrderEntity]:

        curr_session = self._session()
        data = curr_session.query(OrderHeaderModel).get(order_id)
        order_dataclass = OrderRepository._map_rep_dataclass(data)
        curr_session.close()
        return [order_dataclass]

    def read_all(self) -> List[OrderEntity]:

        curr_session = self._session()
        data = curr_session.query(OrderHeaderModel).all()
        order_list = []
        for order in data:
            order_dataclass = OrderRepository._map_rep_dataclass(order)
            order_list.append(order_dataclass)
        curr_session.close()
        return order_list

    def delete_one(self, order_id: int) -> OrderEntity:

        curr_session = self._session()
        order_data = curr_session.query(OrderHeaderModel).get(order_id)
        order_data.status_code = '10'
        curr_session.add(order_data)
        curr_session.commit()
        order_dataclass = OrderRepository._map_rep_dataclass(order_data)
        curr_session.close()
        return order_dataclass

    def update_one(self, order_entity: OrderEntity) -> OrderEntity:

        curr_session = self._session()
        items = order_entity.items
        order_rec = curr_session.query(OrderHeaderModel).get(order_entity.order_id)
        updated_header = OrderHeaderModel(
                                     order_id=order_entity.order_id,
                                     amount=order_entity.amount,
                                     vat_amount=order_entity.vat_amount,
                                     quantity=order_entity.quantity,
                                     weight=order_entity.weight,
                                     city=order_rec.city,
                                     status_code=order_entity.status_code,
                                     created_on=order_rec.created_on,
                                     created_by=order_rec.created_by,
                                     customer_no=order_rec.customer_no)
        updated_header.order_id = order_entity.order_id
        curr_session.merge(updated_header)
        i = 0
        for item in items:
            updated_item = OrderItemModel(
                order_id=order_entity.order_id, item_no=(i+1)*10,
                good_id=item.good_id,
                good_name=item.good_name, quantity=item.quantity)
            curr_session.merge(updated_item)
            i = i + 1
        curr_session.commit()

        data = curr_session.query(OrderHeaderModel).get(order_entity.order_id)
        order_dataclass = OrderRepository._map_rep_dataclass(rep_data=data)
        curr_session.close()
        return order_dataclass

    def create_one(self, order_entity: OrderEntity) -> OrderEntity:

        curr_session = self._session()
        items = order_entity.items
        created_header = OrderHeaderModel(
            order_id=order_entity.order_id,
            amount=order_entity.amount, vat_amount=order_entity.vat_amount,
            quantity=order_entity.quantity, weight=order_entity.weight,
            city=order_entity.city, status_code='01',
            created_on=datetime.now(), created_by=order_entity.created_by,
            customer_no=order_entity.customer_no)

        curr_session.add(created_header)
        i = 0
        for item in items:
            created_item = OrderItemModel(
                order_id=order_entity.order_id, item_no=(i + 1) * 10,
                good_id=item.good_id,
                good_name=item.good_name, quantity=item.quantity)
            curr_session.add(created_item)
            i = i + 1

        curr_session.commit()

        data = curr_session.query(OrderHeaderModel).get(created_header.order_id)
        order_dataclass = OrderRepository._map_rep_dataclass(rep_data=data)
        curr_session.close()
        return order_dataclass
