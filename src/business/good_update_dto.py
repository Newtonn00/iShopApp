from dataclasses import dataclass


@dataclass
class GoodUpdateDto():
    good_id: int
    name: str
    category: str
    availqty: int
    status_code: str
