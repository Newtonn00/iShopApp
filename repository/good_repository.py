from entity.good_entity import GoodEntity
from controller.repo_connection import EngineConnection
from repository.good_repo_entity import GoodItemModel


class GoodRepository:

    def __init__(self, engine_connection: EngineConnection):
        self._session = engine_connection.session

    def _map_rep_dataclass(rep_data) -> GoodEntity:
        good_dataclass = GoodEntity(
            good_id=rep_data.good_id,
            name=rep_data.name,
            category=rep_data.category,
            availqty=rep_data.availqty,
            status_code=rep_data.status_code.rstrip())

        return good_dataclass

    def get_goods_count(self) -> int:
        goods_count: int
        curr_session = self._session()
        goods_count = curr_session.query(GoodItemModel).count()

        return goods_count

    def read_one(self, good_id: int) -> GoodEntity:
        curr_session = self._session()

        data = curr_session.query(GoodItemModel).get(good_id)
        good_dataclass2 = GoodRepository._map_rep_dataclass(data)
        curr_session.close()
        return good_dataclass2

    def delete_one(self, good_id: int) -> GoodEntity:

        curr_session = self._session()
        orig_data = curr_session.query(GoodItemModel).get(good_id)
        orig_data.status_code = '10'
        curr_session.add(orig_data)
        curr_session.commit()
        good_dataclass = GoodRepository._map_rep_dataclass(orig_data)
        curr_session.close()
        return good_dataclass

    def create_one(self, good_entity: GoodEntity) -> GoodEntity:
        curr_session = self._session()
        created_good = GoodItemModel(name=good_entity.name,
                                     category=good_entity.category,
                                     availqty=good_entity.availqty,
                                     status_code='10')
        curr_session.add(created_good)
        curr_session.commit()

        good_dataclass = GoodRepository._map_rep_dataclass(created_good)

        curr_session.close()

        return good_dataclass

    def update_one(self, good_entity: GoodEntity) -> GoodEntity:
        curr_session = self._session()
        updated_good = GoodItemModel(name=good_entity.name,
                                     category=good_entity.category,
                                     availqty=good_entity.availqty,
                                     status_code='10')
        updated_good.good_id = good_entity.good_id
        curr_session.merge(updated_good)
        curr_session.commit()

        data = curr_session.query(GoodItemModel).get(good_entity.good_id)
        good_dataclass = GoodRepository._map_rep_dataclass(data)
        curr_session.close()
        return good_dataclass
