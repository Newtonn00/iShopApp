from src.repository.order_repository import OrderRepository
from src.entity.order_entity import OrderEntity
from src.entity.order_item_entity import OrderItemEntity
from src.business.order_create_dto import OrderCreateDto
from src.business.order_update_dto import OrderUpdateDto


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

        orders_count = self._order_repo.get_order_count(order_dto.customer_no)
        order_no = order_dto.customer_no + str(orders_count)
        order_id = int(order_no)
        order_entity = OrderEntity(order_id=order_id,
                                   city=order_dto.city,
                                   amount=order_dto.amount,
                                   vat_amount=order_dto.vat_amount,
                                   quantity=order_dto.quantity,
                                   weight=order_dto.weight,
                                   customer_no=order_dto.customer_no,
                                   created_by=order_dto.created_by,
                                   created_on=order_dto.created_on,
                                   status_code=order_dto.status_code,
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
                                   status_code=order_dto.status_code,
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
