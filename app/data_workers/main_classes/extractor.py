from database_connectors.mysql_conn import MSQLConnector
from SQL_Query.queries import QUERIES
from logs.logger.logger import Logger


class Extractor:
    def __init__(self):
        self._db_worker = MSQLConnector()
        self._logger = Logger(self)

    def get_data_msq(self):

        self._logger.info(f'start extracting data key: ')

        return self._db_worker.select_people()


if __name__ == '__main__':
    a = Extractor()
    print(a.get_data_msq(key='cards', limit=150))
