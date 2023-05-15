from flask import Flask, request
from flask_restful import Api, Resource
from good_service import GoodService
from marshmallow import ValidationError
from good_http_dto_schema import GoodHttpDtoSchema
import json
from good_entity import GoodEntity


app = Flask(__name__)
api = Api()


class GoodHandler(Resource):

    def _map_json_dataclass(json_data: dict) -> GoodEntity:
        good_dataclass = GoodEntity(
            good_id=json_data["good_id"],
            name=json_data["name"],
            category=json_data["category"],
            availqty=json_data["availqty"],
            status=json_data["status"])

        return good_dataclass

    def get(self, good_id: int):
        good_srv = GoodService()
        try:
            good_data = good_srv.get(good_id)
        except Exception as err:
            return ("Error", str(err)), 400
        good_schema = GoodHttpDtoSchema()
        json_order = good_schema.dump(obj=good_data)
        return json_order, 200

    def delete(self, good_id: int):
        good_srv = GoodService()
        try:
            deleted_good = good_srv.delete(good_id)
        except Exception as err:
            return ("Error", str(err)), 400
        good_schema = GoodHttpDtoSchema()
        json_order = good_schema.dump(obj=deleted_good)
        return json_order, 200

    def post(self, good_id: int):
        good_schema = GoodHttpDtoSchema()
        try:
            input_json: str = json.dumps(request.get_json())
            validated_data = good_schema.loads(json_data=input_json)
        except ValidationError as err:
            return ("Error", err.messages), 422
        good_srv = GoodService(GoodHandler._map_json_dataclass(validated_data))
        try:
            created_good = good_srv.create()
        except Exception as err:
            return ("Error", str(err)), 400
        json_good = good_schema.dump(obj=created_good)
        return json_good, 201

    def put(self, good_id: int):
        good_schema = GoodHttpDtoSchema()
        try:
            input_json: str = json.dumps(request.get_json())
            validated_data = good_schema.loads(json_data=input_json)
        except ValidationError as err:
            return ("Error", err.messages), 422
        good_srv = GoodService(GoodHandler._map_json_dataclass(validated_data))
        try:
            updated_good = good_srv.update()
        except Exception as err:
            return ("Error", str(err)), 400
        json_good = good_schema.dump(obj=updated_good)
        return json_good, 201

api.add_resource(GoodHandler,"/api/good/<int:good_id>")
api.init_app(app)
if __name__ == "__main__":
    app.run(debug=True, port=5000, host="127.0.0.1")