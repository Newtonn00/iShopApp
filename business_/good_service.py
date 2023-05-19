from good_repository import GoodRepository
from good_entity import GoodEntity
from good_dto import GoodDto


class GoodService:
    def __init__(self, good_repo: GoodRepository):
        self._good_rep = good_repo

    def get(self, good_id: int) -> GoodEntity:
        good_dataclass = self._good_rep.read_one(good_id)
        return good_dataclass

    def delete(self, good_id: int) -> GoodEntity:
        good_dataclass = self._good_rep.delete_one(good_id)
        return good_dataclass

    def create(self, good_dto: GoodDto) -> GoodEntity:

        print(good_dto)
        good_entity = GoodEntity(
            good_id=0,
            name=good_dto.name,
            category=good_dto.category,
            availqty=good_dto.availqty,
            status=good_dto.status)

        good_dataclass = self._good_rep.create_one(good_entity)
        return good_dataclass

    def update(self, good_id: int, good_dto: GoodDto) -> GoodEntity:
        good_entity = GoodEntity(
            good_id=good_id,
            name=good_dto.name,
            category=good_dto.category,
            availqty=good_dto.availqty,
            status=good_dto.status)
        good_dataclass = self._good_rep.update_one(good_entity)
        return good_dataclass
