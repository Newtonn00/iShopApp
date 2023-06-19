from flask import Flask
from flask_restful import Api
from order_handler import OrderController
from good_handler import GoodController
from containers import Containers

app = Flask(__name__)
api = Api()
api.add_resource(OrderController, "/api/order/<int:order_id>")
api.add_resource(GoodController, "/api/good/<int:good_id>")
api.init_app(app)
if __name__ == "__main__":
    container = Containers()
    app.run(debug=True, port=5000, host="0.0.0.0")
