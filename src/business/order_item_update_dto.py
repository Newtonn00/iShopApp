from dataclasses import dataclass


@dataclass
class OrderItemUpdateDto:
    item_no: int
    good_id: int
    good_name: str
    quantity: int
