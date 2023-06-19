from dataclasses import dataclass
from datetime import datetime
from src.business.order_item_update_dto import OrderItemUpdateDto


@dataclass
class OrderUpdateDto:
    order_id: int
    city: str
    amount: float
    vat_amount: float
    quantity: int
    weight: float
    status_code: str
    created_on: datetime
    created_by: str
    customer_no: str
    items: list[OrderItemUpdateDto]
