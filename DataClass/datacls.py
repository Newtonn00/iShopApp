from dataclasses import dataclass
from datetime import datetime


@dataclass
class Item_Dataclass():
    order_id: int
    item_no: int
    good_id: int
    good_name: str
    quantity: int


@dataclass
class Order_Dataclass():
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
    items: list[Item_Dataclass]


@dataclass
class Good_Dataclass():
    good_id: int
    name: str
    category: str
    availqty: int
    status: int