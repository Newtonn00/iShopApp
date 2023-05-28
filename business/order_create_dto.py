from dataclasses import dataclass
from datetime import datetime
from business.order_item_create_dto import OrderItemCreateDto


@dataclass
class OrderCreateDto:
    city: str
    amount: float
    vat_amount: float
    quantity: int
    weight: float
    status: int
    created_on: datetime
    created_by: str
    customer_no: str
    items: list[OrderItemCreateDto]
