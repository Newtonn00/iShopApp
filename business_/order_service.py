from order_repository import OrderRepository
from order_entity import OrderEntity
from order_item_entity import OrderItemEntity
from order_dto import OrderDto


class OrderService:

    def __init__(self, order_repo: OrderRepository):
        self._order_repo = order_repo

    def get(self, order_id: int) -> OrderEntity:
        order_dataclass = self._order_repo.read_one(order_id)
        return order_dataclass

    def delete(self, order_id: int) -> OrderEntity:
        order_dataclass = self._order_repo.delete_one(order_id)
        return order_dataclass

    def create(self, order_dto: OrderDto) -> OrderEntity:
        order_entity = OrderEntity(order_id=0,
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
            order_entity.items.insert(i, (OrderItemEntity(
                order_id=0,
                item_no=order_dto.items[i].item_no,
                good_id=order_dto.items[i].good_id,
                good_name=order_dto.items[i].good_name,
                quantity=order_dto.items[i].quantity)))

        order_entity_new = self._order_repo.create_one(order_entity)
        return order_entity_new

    def update(self, order_id: int, order_dto: OrderDto) -> OrderEntity:

        order_entity = OrderEntity(order_id=order_id,
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
            order_entity.items.insert(i, (OrderItemEntity(
                order_id=order_id,
                item_no=order_dto.items[i].item_no,
                good_id=order_dto.items[i].good_id,
                good_name=order_dto.items[i].good_name,
                quantity=order_dto.items[i].quantity)))

        order_entity_new = self._order_repo.update_one(order_entity)
        return order_entity_new
