from DB_Connectors.MYSQL import MYSQLConnector
from SQL_Query.Queryes import Query
from logs.Logger.Loger import DataLogger


class DataExtractor:
    def __init__(self):
        self._db_worker = MYSQLConnector()
        self._logger = DataLogger(self)

    def get_data(self, key: str, limit):
        if limit:

            self._logger.info(f'start extracting data key: {Query[key]} limit {limit}')

            return self._db_worker.fetch(f"{Query[key]} limit {limit}")
        else:

            self._logger.info(f'start extracting data key: {Query[key]}')

            return self._db_worker.fetch(Query[key])


if __name__ == '__main__':
    a = DataExtractor()
    print(a.get_data(key='cards', limit=150))
