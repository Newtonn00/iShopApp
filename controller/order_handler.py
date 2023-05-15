from flask import Flask, request
from flask_restful import Api, Resource
from order_service import OrderService
from marshmallow import ValidationError
import json
from order_item_entity import OrderItemEntity
from order_entity import OrderEntity
from order_http_dto_schema import OrderHttpDtoSchema
import logging

logging.basicConfig(filename="py_log.py",filemode="w",level=logging.INFO)


class OrderHandler(Resource):

    def _map_json_dataclass(json_data: dict) -> OrderEntity:
        order_dataclass = OrderEntity(order_id=json_data["order_id"],
                                          city=json_data["city"],
                                          amount=json_data["amount"],
                                          vat_amount=json_data["vat_amount"],
                                          quantity=json_data["quantity"],
                                          weight=json_data["weight"],
                                          customer_no=json_data["customer_no"],
                                          created_by=json_data["created_by"],
                                          created_on=json_data["created_on"],
                                          status=json_data["status"],
                                          items=[])
        for i in range(json_data["items"].__len__()):
            order_dataclass.items.insert(i, (OrderItemEntity(
                order_id=json_data["items"][i]["order_id"],
                item_no=json_data["items"][i]["item_no"],
                good_id=json_data["items"][i]["good_id"],
                good_name=json_data["items"][i]["good_name"],
                quantity=json_data["items"][i]["quantity"])))
        return order_dataclass

    def get(self, order_id: int):
        order_srv = OrderService()
        try:
            order_data = order_srv.get(order_id)
        except Exception as err:
            logging.error(str(err), exc_info=True)
            return {"Error": "internal server error"}, 500
        order_schema = OrderHttpDtoSchema()
        order_json = order_schema.dump(obj=order_data)
        return order_json, 200

    def delete(self, order_id: int):
        order_srv = OrderService()
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
        order_srv = OrderService(OrderHandler._map_json_dataclass(validated_data))
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
        order_srv = OrderService(OrderHandler._map_json_dataclass(validated_data))
        try:
            updated_order = order_srv.update()
        except Exception as err:
            logging.error(str(err), exc_info=True)
            return {"Error": "internal server error"}, 500
        order_json = order_schema.dump(obj=updated_order)
        return order_json, 200

