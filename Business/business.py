from Repository.repository import OrderRepository, GoodRepository
from datacls import Order_Dataclass, Good_Dataclass

orderDS = OrderRepository()
goodDS = GoodRepository()


class OrderBusinessLogic():
    def get(self, order_id: int) -> Order_Dataclass:
        order_dataclass = orderDS.read_one(order_id)
        return order_dataclass

    def delete(self, order_id: int) -> Order_Dataclass:
        order_dataclass = orderDS.delete_one(order_id)
        return order_dataclass

    def create(self, order_data: Order_Dataclass) -> Order_Dataclass:
        order_dataclass = orderDS.create_one(order_data)
        return order_dataclass

    def update(self,
               order_data: Order_Dataclass) -> Order_Dataclass:
        order_dataclass = orderDS.update_one(order_data)
        return order_dataclass


class GoodBusinessLogic():
    def get(self, good_id: int) -> Good_Dataclass:
        good_dataclass = goodDS.read_one(good_id)
        return good_dataclass

    def delete(self, good_id: int) -> Good_Dataclass:
        good_dataclass = goodDS.delete_one(good_id)
        return good_dataclass

    def create(self, good_data: Good_Dataclass) -> Good_Dataclass:
        good_dataclass = goodDS.create_one(good_data)
        return good_dataclass

    def update(self,
               good_data: Good_Dataclass) -> Good_Dataclass:
        good_dataclass = goodDS.update_one(good_data)
        return good_dataclass
