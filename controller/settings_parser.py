import configparser
import os
from controller.settings_error import SettingsError


class SettingsParser:
    db_user_name: str
    db_name: str
    db_host: str
    db_password: str

    def __init__(self):

        _settings_file_exists = True
        config = configparser.ConfigParser()
        if os.path.exists(os.environ.get('WORKDIR')+'/settings.ini') is False:
            _settings_file_exists = False
        else:
            config.read('/settings.ini')

        if os.environ.get('DB_NAME') == '' and _settings_file_exists and config.has_option('db','db_name'):
            self.db_name = config['db']['db_name']
        else:
            self.db_name = os.environ.get('DB_NAME')

        if os.environ.get('DB_HOST') == '' and _settings_file_exists and config.has_option('db','db_host'):
            self.db_host = config['db']['db_host']
        else:
            self.db_host = os.environ.get('DB_HOST')

        if os.environ.get('DB_USER_NAME') == '' and _settings_file_exists and config.has_option('db','db_user_name'):
            self.db_user_name = config['db']['db_user_name']
        else:
            self.db_user_name = os.environ.get('DB_USER_NAME')

        if os.environ.get('DB_PASSWORD') == '' and _settings_file_exists and config.has_option('db','db_password'):
            self.db_password = config['db']['db_password']
        else:
            self.db_password = os.environ.get('DB_PASSWORD')

        if (self.db_name == '') or (self.db_user_name == '') or (self.db_host == '') or (self.db_password == ''):
            raise SettingsError()
