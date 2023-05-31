from flask import Flask
from flask_restful import Api
from controller.good_handler import GoodController
from controller.order_handler import OrderController
from controller.containers import Containers

app = Flask(__name__)
api = Api()
api.add_resource(OrderController, "/api/order/<int:order_id>")
api.add_resource(GoodController, "/api/good/<int:good_id>")
api.init_app(app)
if __name__ == "__main__":
    container = Containers()
#    engine_connection = container.engine_connection()
    app.run(debug=False, port=5000, host="127.0.0.1")
