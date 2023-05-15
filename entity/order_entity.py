from dataclasses import dataclass
from datetime import datetime
from order_item_entity import OrderItemEntity


@dataclass
class OrderEntity():
    order_id: int
    city: str
    amount: float
    vat_amount: float
    quantity: int
    weight: float
    status: int
    created_on: datetime
    created_by: str
    customer_no: str
    items: list[OrderItemEntity]