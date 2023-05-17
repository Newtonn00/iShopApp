import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, String
from good_entity import GoodEntity
from repo_connection import EngineConnection

Base = declarative_base()

class GoodItem(Base):
    __tablename__ = 'good'
    good_id = sa.Column(Integer, primary_key=True)
    name = sa.Column(String, nullable=False)
    category = sa.Column(String, default='99')
    availqty = sa.Column(Integer, default=0)
    status = sa.Column(Integer, nullable=False)

    def __init__(self, name: str, category: str, availqty: int, status: int):
        self.name = name
        self.category = category
        self.availqty = availqty
        self.status = status


class GoodRepository():

    def __init__(self, engine_connection: EngineConnection,
                 good_entity: GoodEntity = None):
        self._good_entity = good_entity
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

    def create_one(self) -> GoodEntity:
        curr_session = self._session()
        created_good = GoodItem(name=self._good_entity.name,
                                category=self._good_entity.category,
                                availqty=self._good_entity.availqty,
                                status=self._good_entity.status)
        curr_session.add(created_good)
        curr_session.commit()
        good_dataclass = GoodRepository._map_rep_dataclass(created_good)

        curr_session.close()

        return good_dataclass

    def update_one(self) -> GoodEntity:
        curr_session = self._session()
        updated_good = GoodItem(name=self._good_entity.name,
                                category=self._good_entity.category,
                                availqty=self._good_entity.availqty,
                                status=self._good_entity.status)
        updated_good.good_id = self._good_entity.good_id
        curr_session.merge(updated_good)
        curr_session.commit()

        data = curr_session.query(GoodItem).get(self._good_entity.good_id)
        good_dataclass = GoodRepository._map_rep_dataclass(data)
        curr_session.close()
        return good_dataclass
