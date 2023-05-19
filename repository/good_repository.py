from good_entity import GoodEntity
from repo_connection import EngineConnection
from good_repo_entity import GoodItem


class GoodRepository:

    def __init__(self, engine_connection: EngineConnection):
        self._session = engine_connection.session

    def _map_rep_dataclass(rep_data) -> GoodEntity:
        good_dataclass = GoodEntity(
            good_id=rep_data.good_id,
            name=rep_data.name,
            category=rep_data.category,
            availqty=rep_data.availqty,
            status=rep_data.status)

        return good_dataclass

    def read_one(self, good_id: int) -> GoodEntity:
        curr_session = self._session()

        data = curr_session.query(GoodItem).get(good_id)
        good_dataclass = GoodRepository._map_rep_dataclass(data)
        curr_session.close()
        return good_dataclass

    def delete_one(self, good_id: int) -> GoodEntity:

        curr_session = self._session()
        orig_data = curr_session.query(GoodItem).get(good_id)
        orig_data.status = 10
        curr_session.add(orig_data)
        curr_session.commit()
        good_dataclass = GoodRepository._map_rep_dataclass(orig_data)
        curr_session.close()
        return good_dataclass

    def create_one(self, good_entity: GoodEntity) -> GoodEntity:
        curr_session = self._session()
        created_good = GoodItem(name=good_entity.name,
                                category=good_entity.category,
                                availqty=good_entity.availqty,
                                status=good_entity.status)
        curr_session.add(created_good)
        curr_session.commit()
        good_dataclass = GoodRepository._map_rep_dataclass(created_good)

        curr_session.close()

        return good_dataclass

    def update_one(self, good_entity: GoodEntity) -> GoodEntity:
        curr_session = self._session()
        updated_good = GoodItem(name=good_entity.name,
                                category=good_entity.category,
                                availqty=good_entity.availqty,
                                status=good_entity.status)
        updated_good.good_id = good_entity.good_id
        curr_session.merge(updated_good)
        curr_session.commit()

        data = curr_session.query(GoodItem).get(good_entity.good_id)
        good_dataclass = GoodRepository._map_rep_dataclass(data)
        curr_session.close()
        return good_dataclass
