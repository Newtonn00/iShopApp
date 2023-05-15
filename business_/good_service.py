from good_repository import GoodRepository
from good_entity import GoodEntity



class GoodService():
    def __init__(self, good_entity: GoodEntity):
        self._good_entity = good_entity
    def get(self, good_id: int) -> GoodEntity:
        good_rep = GoodRepository()
        good_dataclass = good_rep.read_one(good_id)
        return good_dataclass

    def delete(self, good_id: int) -> GoodEntity:
        good_rep = GoodRepository()
        good_dataclass = good_rep.delete_one(good_id)
        return good_dataclass

    def create(self) -> GoodEntity:
        good_rep = GoodRepository(self._good_entity)
        good_dataclass = good_rep.create_one()
        return good_dataclass

    def update(self) -> GoodEntity:
        good_rep = GoodRepository(self._good_entity)
        good_dataclass = good_rep.update_one()
        return good_dataclass
