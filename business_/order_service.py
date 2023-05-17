from order_repository import OrderRepository
from order_entity import OrderEntity
from order_item_entity import OrderItemEntity
from repo_connection import EngineConnection
from order_dto import OrderDto


class OrderService:

    def __init__(self, engine_connection: EngineConnection,
                 order_dto: OrderDto = None):
        self._order_dto = order_dto
        self._engine_connection = engine_connection

    def _map_dto_to_entity(self, order_id: int, order_dto: OrderDto) -> OrderEntity:
        order_dataclass = OrderEntity(order_id=order_id,
                                      city=order_dto.city,
                                      amount=order_dto.amount,
                                      vat_amount=order_dto.vat_amount,
                                      quantity=order_dto.quantity,
                                      weight=order_dto.weight,
                                      customer_no=order_dto.customer_no,
                                      created_by=order_dto.created_by,
                                      created_on=order_dto.created_on,
                                      status=order_dto.status,
                                      items=[])
        for i in range(len(order_dto.items)):
            order_dataclass.items.insert(i, (OrderItemEntity(
                order_id=order_id,
                item_no=order_dto.items[i].item_no,
                good_id=order_dto.items[i].good_id,
                good_name=order_dto.items[i].good_name,
                quantity=order_dto.items[i].quantity)))
        return order_dataclass

    def get(self, order_id: int) -> OrderEntity:
        order_rep = OrderRepository(engine_connection=self._engine_connection)
        order_dataclass = order_rep.read_one(order_id)
        return order_dataclass

    def delete(self, order_id: int) -> OrderEntity:
        order_rep = OrderRepository(engine_connection=self._engine_connection)
        order_dataclass = order_rep.delete_one(order_id)
        return order_dataclass

    def create(self) -> OrderEntity:
        order_rep = OrderRepository(order_entity=self._map_dto_to_entity(0,self._order_dto),
                                    engine_connection=self._engine_connection)
        order_dataclass = order_rep.create_one()
        return order_dataclass

    def update(self,order_id: int) -> OrderEntity:
        order_rep = OrderRepository(order_entity=self._map_dto_to_entity(order_id,self._order_dto),
                                    engine_connection=self._engine_connection)
        order_dataclass = order_rep.update_one()
        return order_dataclass
