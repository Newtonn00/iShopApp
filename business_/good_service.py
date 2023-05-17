from good_repository import GoodRepository
from good_entity import GoodEntity
from good_dto import GoodDto
from repo_connection import EngineConnection



class GoodService():
    def __init__(self, engine_connection: EngineConnection,
                 good_dto: GoodDto = None):
        self._good_dto = good_dto
        self._engine_connection = engine_connection
    def _map_dto_to_entity(self,good_id: int,
                           good_dto: GoodDto) -> GoodEntity:
        good_entity = GoodEntity(
            good_id=good_id,
            name=good_dto.name,
            category=good_dto.category,
            availqty=good_dto.availqty,
            status=good_dto.status)
        return good_entity

    def get(self, good_id: int) -> GoodEntity:
        good_rep = GoodRepository(engine_connection=self._engine_connection)
        good_dataclass = good_rep.read_one(good_id)
        return good_dataclass

    def delete(self, good_id: int) -> GoodEntity:
        good_rep = GoodRepository(engine_connection=self._engine_connection)
        good_dataclass = good_rep.delete_one(good_id)
        return good_dataclass

    def create(self) -> GoodEntity:
        good_rep = GoodRepository(good_entity=self._map_dto_to_entity(0, self._good_dto),
                                  engine_connection=self._engine_connection)
        good_dataclass = good_rep.create_one()
        return good_dataclass

    def update(self, good_id: int) -> GoodEntity:
        good_rep = GoodRepository(good_entity=self._map_dto_to_entity(good_id, self._good_dto),
                                  engine_connection=self._engine_connection)
        good_dataclass = good_rep.update_one()
        return good_dataclass
