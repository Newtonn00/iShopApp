from dataclasses import dataclass


@dataclass
class OrderItemEntity():
    order_id: int
    item_no: int
    good_id: int
    good_name: str
    quantity: int