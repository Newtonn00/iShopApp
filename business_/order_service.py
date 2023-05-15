from order_repository import OrderRepository
from order_entity import OrderEntity


class OrderService():

    def __init__(self, order_entity: OrderEntity):
        self._order_entity = order_entity

    def get(self, order_id: int) -> OrderEntity:
        order_rep = OrderRepository()
        order_dataclass = order_rep.read_one(order_id)
        return order_dataclass

    def delete(self, order_id: int) -> OrderEntity:
        order_rep = OrderRepository()
        order_dataclass = order_rep.delete_one(order_id)
        return order_dataclass

    def create(self) -> OrderEntity:
        order_rep = OrderRepository(self._order_entity)
        order_dataclass = order_rep.create_one()
        return order_dataclass

    def update(self) -> OrderEntity:
        order_rep = OrderRepository(self._order_entity)
        order_dataclass = order_rep.update_one()
        return order_dataclass
