from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
import json

from src.business.order_item_create_dto import OrderItemCreateDto
from src.business.order_create_dto import OrderCreateDto
from src.business.order_update_dto import OrderUpdateDto
from src.business.order_item_update_dto import OrderItemUpdateDto
from order_http_dto_schema import OrderHttpDtoSchema
import logging
from containers import Containers

logging.basicConfig(filename="py_log.py", filemode="w", level=logging.INFO)
order_srv = Containers.order_service()


class OrderController(Resource):

    def get(self, order_id: int):

        try:
            order_data = order_srv.get(order_id)
        except Exception as err:
            logging.error(str(err), exc_info=True)
            return {"Error": "internal server error"}, 500
        order_schema = OrderHttpDtoSchema()
        order_json = order_schema.dump(obj=order_data)
        return order_json, 200

    def delete(self, order_id: int):
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

        order_dto = OrderCreateDto(city=validated_data["city"],
                                   amount=validated_data["amount"],
                                   vat_amount=validated_data["vat_amount"],
                                   quantity=validated_data["quantity"],
                                   weight=validated_data["weight"],
                                   customer_no=validated_data["customer_no"],
                                   created_by=validated_data["created_by"],
                                   created_on=validated_data["created_on"],
                                   status_code=validated_data["status_code"],
                                   items=[])
        for i in range(len(validated_data["items"])):
            order_dto.items.insert(i, (OrderItemCreateDto(
                item_no=validated_data["items"][i]["item_no"],
                good_id=validated_data["items"][i]["good_id"],
                good_name=validated_data["items"][i]["good_name"],
                quantity=validated_data["items"][i]["quantity"])))

        try:
            created_order = order_srv.create(order_dto=order_dto)
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

        order_dto = OrderUpdateDto(order_id=validated_data["order_id"],
                                   city=validated_data["city"],
                                   amount=validated_data["amount"],
                                   vat_amount=validated_data["vat_amount"],
                                   quantity=validated_data["quantity"],
                                   weight=validated_data["weight"],
                                   customer_no=validated_data["customer_no"],
                                   created_by=validated_data["created_by"],
                                   created_on=validated_data["created_on"],
                                   status_code=validated_data["status_code"],
                                   items=[])
        for i in range(len(validated_data["items"])):
            order_dto.items.insert(i, (OrderItemUpdateDto(
                item_no=validated_data["items"][i]["item_no"],
                good_id=validated_data["items"][i]["good_id"],
                good_name=validated_data["items"][i]["good_name"],
                quantity=validated_data["items"][i]["quantity"])))

        try:
            updated_order = order_srv.update(order_dto)
        except Exception as err:
            logging.error(str(err), exc_info=True)
            return {"Error": "internal server error"}, 500
        order_json = order_schema.dump(obj=updated_order)
        return order_json, 200

