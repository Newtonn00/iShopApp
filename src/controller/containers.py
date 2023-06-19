from dependency_injector import containers, providers
from repo_connection import EngineConnection
from src.business.good_service import GoodService
from src.repository.good_repository import GoodRepository
from src.business.order_service import OrderService
from src.repository.order_repository import OrderRepository


class Containers(containers.DeclarativeContainer):

    engine_connection = providers.Singleton(EngineConnection)
    good_repo = providers.Factory(GoodRepository,
                                  engine_connection=engine_connection)
    good_service = providers.Factory(GoodService,
                                     good_repo=good_repo)

    order_repo = providers.Factory(OrderRepository,
                                   engine_connection=engine_connection)
    order_service = providers.Factory(OrderService,
                                      order_repo=order_repo)
