from flask import Flask, request
from flask_restful import Api, Resource
from Business.business import OrderBusinessLogic, GoodBusinessLogic
from marshmallow import Schema, fields, ValidationError
import json
from DataClass.datacls import Order_Dataclass, Item_Dataclass, Good_Dataclass


app = Flask(__name__)
api = Api()
order_bl = OrderBusinessLogic()
good_bl = GoodBusinessLogic()


class GoodSchema(Schema):
    good_id = fields.Integer()
    name = fields.Str()
    category = fields.Str()
    availqty = fields.Integer()
    status = fields.Integer()


class ItemSchema(Schema):
    order_id = fields.Integer()
    item_no = fields.Integer()
    good_id = fields.Integer()
    good_name = fields.Str()
    quantity = fields.Integer()


class OrderSchema(Schema):
    order_id = fields.Integer()
    city = fields.Str()
    status = fields.Integer()
    amount = fields.Float()
    vat_amount = fields.Float()
    weight = fields.Integer()
    created_on = fields.DateTime()
    created_by = fields.Str()
    quantity = fields.Integer()
    customer_no = fields.Str()
    items = fields.List(fields.Nested(ItemSchema))

#    @post_load
#    def make_mapping(self, data, **kwargs):
#        return Order_Dataclass(**data)


class OrderController(Resource):

    def map_json_dataclass(json_data: dict) -> Order_Dataclass:
        order_dataclass = Order_Dataclass(order_id=json_data["order_id"],
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
            order_dataclass.items.insert(i, (Item_Dataclass(
                order_id=json_data["items"][i]["order_id"],
                item_no=json_data["items"][i]["item_no"],
                good_id=json_data["items"][i]["good_id"],
                good_name=json_data["items"][i]["good_name"],
                quantity=json_data["items"][i]["quantity"])))
        return order_dataclass

    def get(self, order_id: int):
        order_data = order_bl.get(order_id)
        order_schema = OrderSchema()
        json_order = order_schema.dump(obj=order_data)
        return json_order, 200

    def delete(self, order_id: int):
        deleted_order = order_bl.delete(order_id)
        order_schema = OrderSchema()
        json_order = order_schema.dump(obj=deleted_order)
        return json_order, 200

    def post(self, order_id: int):
        order_schema = OrderSchema()
        try:
            input_json: str = json.dumps(request.get_json())
            validated_data = order_schema.loads(json_data=input_json)
        except ValidationError as err:
            return ("Error", err.messages), 422
        order_dataclass = OrderController.map_json_dataclass(validated_data)
        created_order = order_bl.create(order_dataclass)
        json_order = order_schema.dump(obj=created_order)
        return json_order, 201

    def put(self, order_id: int):
        order_schema = OrderSchema()
        try:
            input_json: str = json.dumps(request.get_json())
            validated_data = order_schema.loads(json_data=input_json)
        except ValidationError as err:
            return ("Error", err.messages), 422
        order_dataclass = OrderController.map_json_dataclass(validated_data)
        updated_order = order_bl.update(order_dataclass)
        json_order = order_schema.dump(obj=updated_order)
        return json_order, 201


class GoodController(Resource):

    def map_json_dataclass(json_data: dict) -> Good_Dataclass:
        good_dataclass = Good_Dataclass(
            good_id=json_data["good_id"],
            name=json_data["name"],
            category=json_data["category"],
            availqty=json_data["availqty"],
            status=json_data["status"])

        return good_dataclass

    def get(self, good_id: int):
        good_data = good_bl.get(good_id)
        good_schema = GoodSchema()
        json_order = good_schema.dump(obj=good_data)
        return json_order, 200

    def delete(self, good_id: int):
        deleted_good = good_bl.delete(good_id)
        good_schema = GoodSchema()
        json_order = good_schema.dump(obj=deleted_good)
        return json_order, 200

    def post(self, good_id: int):
        good_schema = GoodSchema()
        try:
            input_json: str = json.dumps(request.get_json())
            validated_data = good_schema.loads(json_data=input_json)
        except ValidationError as err:
            return ("Error", err.messages), 422
        good_dataclass = GoodController.map_json_dataclass(validated_data)
        created_good = good_bl.create(good_dataclass)
        json_good = good_schema.dump(obj=created_good)
        return json_good, 201

    def put(self, good_id: int):
        good_schema = GoodSchema()
        try:
            input_json: str = json.dumps(request.get_json())
            validated_data = good_schema.loads(json_data=input_json)
        except ValidationError as err:
            return ("Error", err.messages), 422
        good_dataclass = GoodController.map_json_dataclass(validated_data)
        updated_good = good_bl.update(good_dataclass)
        json_good = good_schema.dump(obj=updated_good)
        return json_good, 201


api.add_resource(OrderController, "/api/order/<int:order_id>")
api.add_resource(GoodController, "/api/good/<int:good_id>")
api.init_app(app)
if __name__ == "__main__":
    app.run(debug=True, port=5000, host="127.0.0.1")
