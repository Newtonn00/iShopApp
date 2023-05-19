from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from good_http_dto_schema import GoodHttpDtoSchema
from good_dto import GoodDto
import logging
from containers import Containers

containers = Containers()
good_srv = containers.good_service()
logging.basicConfig(filename="py_log.py",filemode="w",level=logging.INFO)

class GoodHandler(Resource):

    def _map_json_dataclass(json_data: dict) -> GoodDto:
        good_dataclass = GoodDto(
            name=json_data["name"],
            category=json_data["category"],
            availqty=json_data["availqty"],
            status=json_data["status"])

        return good_dataclass

    def get(self, good_id: int):
        try:
            good_data = good_srv.get(good_id)
        except Exception as err:
            logging.error(str(err),exc_info=True)
            return {"Error": "internal server error"}, 500
        good_schema = GoodHttpDtoSchema()
        good_json = good_schema.dump(obj=good_data)
        return good_json, 200

    def delete(self, good_id: int):
        try:
            deleted_good = good_srv.delete(good_id)
        except Exception as err:
            logging.error(str(err), exc_info=True)
            return {"Error": "internal server error"}, 500
        good_schema = GoodHttpDtoSchema()
        good_json = good_schema.dump(obj=deleted_good)
        return good_json, 200

    def post(self, good_id: int):
        good_schema = GoodHttpDtoSchema()
        try:
            validated_data = good_schema.load(request.get_json())
        except ValidationError as err:
            logging.error(str(err), exc_info=True)
            return {"Error": "validation error"}, 400
        good_dto = GoodHandler._map_json_dataclass(validated_data)
        try:
            created_good = good_srv.create(good_dto=good_dto)
        except Exception as err:
            logging.error(str(err), exc_info=True)
            return {"Error": "internal server error"}, 500
        good_json = good_schema.dump(obj=created_good)
        return good_json, 200

    def put(self, good_id: int):
        good_schema = GoodHttpDtoSchema()
        try:
            validated_data = good_schema.load(request.get_json())
        except ValidationError as err:
            logging.error(str(err), exc_info=True)
            return {"Error": "validation error"}, 400
        good_dto = GoodHandler._map_json_dataclass(validated_data)
        try:
            updated_good = good_srv.update(good_id=good_id,good_dto=good_dto)
        except Exception as err:
            logging.error(str(err), exc_info=True)
            return {"Error": "internal server error"}, 500
        good_json = good_schema.dump(obj=updated_good)
        return good_json, 200

