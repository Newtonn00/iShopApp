from dataclasses import dataclass


@dataclass
class GoodCreateDto():
    name: str
    category: str
    availqty: int
    status_code: str
