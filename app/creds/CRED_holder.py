import configparser

from creds.path_holder.path_holder import PATH


class Cred:
    def __init__(self, param):
        CRED = configparser.ConfigParser()
        CRED.read(PATH)

        self._host = CRED.get(param, 'host')
        self._database = CRED.get(param, 'database')
        self._user = CRED.get(param, 'user')
        self._password = CRED.get(param, 'password')
