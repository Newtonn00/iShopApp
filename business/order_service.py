from repository.order_repository import OrderRepository
from entity.order_entity import OrderEntity
from entity.order_item_entity import OrderItemEntity
from business.order_create_dto import OrderCreateDto
from business.order_update_dto import OrderUpdateDto


class OrderService:

    def __init__(self, order_repo: OrderRepository):
        self._order_repo = order_repo

    def get(self, order_id: int) -> OrderEntity:
        order_entity = self._order_repo.read_one(order_id)
        return order_entity

    def delete(self, order_id: int) -> OrderEntity:
        order_entity = self._order_repo.delete_one(order_id)
        return order_entity

    def create(self, order_dto: OrderCreateDto) -> OrderEntity:
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
        i = 0
        for item in order_dto.items:
            order_entity.items.insert(i, (OrderItemEntity(
                order_id=0,
                item_no=item.item_no,
                good_id=item.good_id,
                good_name=item.good_name,
                quantity=item.quantity)))
            i = i + 1

        order_entity_new = self._order_repo.create_one(order_entity)
        return order_entity_new

    def update(self, order_dto: OrderUpdateDto) -> OrderEntity:

        order_entity = OrderEntity(order_id=order_dto.order_id,
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
        i = 0
        for item in order_dto.items:
            order_entity.items.insert(i, (OrderItemEntity(
                order_id=order_dto.order_id,
                item_no=item.item_no,
                good_id=item.good_id,
                good_name=item.good_name,
                quantity=item.quantity)))
            i = i + 1

        order_entity_new = self._order_repo.update_one(order_entity)
        return order_entity_new
