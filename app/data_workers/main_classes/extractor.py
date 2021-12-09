from database_connectors.mysql import Mconnector
from SQL_Query.queries import QUERIES
from logs.logger.logger import Logger


class Extractor:
    def __init__(self):
        self._db_worker = Mconnector()
        self._logger = Logger(self)

    def get_data_msq(self, key: str, limit):

        self._logger.info(f'start extracting data key: {QUERIES[key]} limit {limit}')

        return self._db_worker.fetch(f"{QUERIES[key]} limit {limit}")


if __name__ == '__main__':
    a = Extractor()
    print(a.get_data_msq(key='cards', limit=150))
