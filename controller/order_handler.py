from flask import Flask, request
from flask_restful import Api, Resource
from order_service import OrderService
from marshmallow import ValidationError
import json
from order_dto import OrderDto
from order_item_dto import OrderItemDto
from order_http_dto_schema import OrderHttpDtoSchema
import logging
from repo_connection import EngineConnection

logging.basicConfig(filename="py_log.py",filemode="w",level=logging.INFO)
engine_connection = EngineConnection()

class OrderHandler(Resource):

    def _map_json_dataclass(json_data: dict) -> OrderDto:
        order_dataclass = OrderDto(city=json_data["city"],
                                   amount=json_data["amount"],
                                   vat_amount=json_data["vat_amount"],
                                   quantity=json_data["quantity"],
                                   weight=json_data["weight"],
                                   customer_no=json_data["customer_no"],
                                   created_by=json_data["created_by"],
                                   created_on=json_data["created_on"],
                                   status=json_data["status"],
                                   items=[])
        for i in range(len(json_data["items"])):
            order_dataclass.items.insert(i, (OrderItemDto(
                item_no=json_data["items"][i]["item_no"],
                good_id=json_data["items"][i]["good_id"],
                good_name=json_data["items"][i]["good_name"],
                quantity=json_data["items"][i]["quantity"])))
        return order_dataclass

    def get(self, order_id: int):
        order_srv = OrderService(engine_connection=engine_connection)
        try:
            order_data = order_srv.get(order_id)
        except Exception as err:
            logging.error(str(err), exc_info=True)
            return {"Error": "internal server error"}, 500
        order_schema = OrderHttpDtoSchema()
        order_json = order_schema.dump(obj=order_data)
        return order_json, 200

    def delete(self, order_id: int):
        order_srv = OrderService(engine_connection=engine_connection)
        try:
            deleted_order = order_srv.delete(order_id)
        except Exception as err:
            logging.error(str(err), exc_info=True)
            return {"Error": "internal server error"}, 500
        order_schema = OrderHttpDtoSchema()
        order_json = order_schema.dump(obj=deleted_order)
        return order_json, 200

    def post(self, order_id: int):
        order_schema = OrderHttpDtoSchema()
        try:
            input_json: str = json.dumps(request.get_json())
            validated_data = order_schema.loads(json_data=input_json)
        except ValidationError as err:
            logging.error(str(err), exc_info=True)
            return {"Error": "validation error"}, 400
        order_srv = OrderService(order_dto=OrderHandler._map_json_dataclass(validated_data),
                                 engine_connection=engine_connection)
        try:
            created_order = order_srv.create()
        except Exception as err:
            logging.error(str(err), exc_info=True)
            return {"Error": "internal server error"}, 500
        order_json = order_schema.dump(obj=created_order)
        return order_json, 200

    def put(self, order_id: int):
        order_schema = OrderHttpDtoSchema()
        try:
            input_json: str = json.dumps(request.get_json())
            validated_data = order_schema.loads(json_data=input_json)
        except ValidationError as err:
            logging.error(str(err), exc_info=True)
            return {"Error": "validation error"}, 400
        order_srv = OrderService(order_dto=OrderHandler._map_json_dataclass(validated_data),
                                 engine_connection=engine_connection)
        try:
            updated_order = order_srv.update()
        except Exception as err:
            logging.error(str(err), exc_info=True)
            return {"Error": "internal server error"}, 500
        order_json = order_schema.dump(obj=updated_order)
        return order_json, 200

