from dataclasses import dataclass


@dataclass
class GoodDto():
    name: str
    category: str
    availqty: int
    status: int