import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from settings_parser import SettingsParser

class EngineConnection:
    def __init__(self):
        connection_settings = SettingsParser()
        self._engine = sa.create_engine(
                       "postgresql+psycopg2://"+connection_settings.db_user_name+":"+
                       connection_settings.db_password+"@"+connection_settings.db_host+"/"+
                       connection_settings.db_name,
                       echo=False, pool_size=5)

        self._engine.connect()
        self.session = sessionmaker(bind=self._engine)
