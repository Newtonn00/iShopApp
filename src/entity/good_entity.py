from dataclasses import dataclass


@dataclass
class GoodEntity():
    good_id: int
    name: str
    category: str
    availqty: int
    status_code: str
