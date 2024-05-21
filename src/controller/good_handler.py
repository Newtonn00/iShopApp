from flask import request, jsonify
from flask_restful import Resource
from marshmallow import ValidationError
from good_http_dto_schema import GoodHttpDtoSchema
from src.business.good_update_dto import GoodUpdateDto
from src.business.good_create_dto import GoodCreateDto
import logging
from containers import Containers

containers = Containers()
good_srv = containers.good_service()
logging.basicConfig(filename="py_log.py", filemode="w", level=logging.INFO)

class GoodController(Resource):

    def get(self, good_id: int):
        try:
            good_data = good_srv.get(good_id)
        except Exception as err:
            logging.error(str(err), exc_info=True)
            return {"Error": "internal server error"}, 500
        good_schema = GoodHttpDtoSchema()
        # good_json = good_schema.dump(obj=good_data)
        good_list = []
        for good_dict in good_data:
            good_list.append(good_schema.dump(obj=good_dict))

        return good_list, 200

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
        good_dto = GoodCreateDto(name=validated_data["name"],
                                 category=validated_data["category"],
                                 availqty=validated_data["availqty"],
                                 status_code=validated_data["status_code"])
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
        good_dto = GoodUpdateDto(good_id=good_id,
                                 name=validated_data["name"],
                                 category=validated_data["category"],
                                 availqty=validated_data["availqty"],
                                 status_code=validated_data["status_code"])
        try:
            updated_good = good_srv.update(good_dto=good_dto)
        except Exception as err:
            logging.error(str(err), exc_info=True)
            return {"Error": "internal server error"}, 500
        good_json = good_schema.dump(obj=updated_good)
        return good_json, 200
