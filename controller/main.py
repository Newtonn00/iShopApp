from flask import Flask
from flask_restful import Api
from repo_connection import EngineConnection
from good_handler import GoodHandler
from order_handler import OrderHandler


app = Flask(__name__)
api = Api()
api.add_resource(OrderHandler, "/api/order/<int:order_id>")
api.add_resource(GoodHandler,"/api/good/<int:good_id>")
api.init_app(app)
if __name__ == "__main__":
    app.run(debug=True, port=5000, host="127.0.0.1")