import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
import configparser

class EngineConnection:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('settings.ini')
        host = config['db']['host']
        user_name = config['db']['user_name']
        db_name = config['db']['db_name']
        password = config['db']['password']
        self._engine = sa.create_engine(
        "postgresql+psycopg2://"+user_name+":"+password+"@"+host+"/"+db_name,
        echo=True, pool_size=5)
        self._engine.connect()
        self.session = sessionmaker(bind=self._engine)
