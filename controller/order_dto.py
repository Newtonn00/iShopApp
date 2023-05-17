from dataclasses import dataclass
from datetime import datetime
from order_item_dto import OrderItemDto


@dataclass
class OrderDto():
    city: str
    amount: float
    vat_amount: float
    quantity: int
    weight: float
    status: int
    created_on: datetime
    created_by: str
    customer_no: str
    items: list[OrderItemDto]