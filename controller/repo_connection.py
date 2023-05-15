import sqlalchemy as sa


class EngineConnection:

     engine = sa.create_engine(
     "postgresql+psycopg2://ishop_admin:Password78@178.20.40.136/ishop_db",
     echo=True, pool_size=5)

     def repo_connect(self):
        engine.connect()