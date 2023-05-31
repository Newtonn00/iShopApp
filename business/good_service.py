from repository.good_repository import GoodRepository
from entity.good_entity import GoodEntity
from business.good_update_dto import GoodUpdateDto
from business.good_create_dto import GoodCreateDto

class GoodService:
    def __init__(self, good_repo: GoodRepository):
        self._good_repo = good_repo

    def get(self, good_id: int) -> GoodEntity:
        good_entity = self._good_repo.read_one(good_id)
        return good_entity

    def delete(self, good_id: int) -> GoodEntity:
        good_entity = self._good_repo.delete_one(good_id)
        return good_entity

    def create(self, good_dto: GoodCreateDto) -> GoodEntity:

        last_good_id = self._good_repo.get_goods_count()

        good_entity = GoodEntity(
            good_id=last_good_id + 1,
            name=good_dto.name,
            category=good_dto.category,
            availqty=good_dto.availqty,
            status_code=good_dto.status_code)

        good_entity = self._good_repo.create_one(good_entity)
        return good_entity

    def update(self, good_dto: GoodUpdateDto) -> GoodEntity:
        good_entity = GoodEntity(
            good_id=good_dto.good_id,
            name=good_dto.name,
            category=good_dto.category,
            availqty=good_dto.availqty,
            status_code=good_dto.status_code)
        good_entity = self._good_repo.update_one(good_entity)
        return good_entity
