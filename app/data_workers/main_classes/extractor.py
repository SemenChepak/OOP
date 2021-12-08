from DB_Connectors.MYSQL import MYSQLConnector
from SQL_Query.Queryes import Query


class DataExtractor:
    def __init__(self):
        self.db_worker = MYSQLConnector()

    def get_data(self, key: str, limit):
        if limit:
            return self.db_worker.fetch(f"{Query[key]} limit {limit}")
        else:
            return self.db_worker.fetch(Query[key])


if __name__ == '__main__':
    a = DataExtractor()
    print(a.get_data(key='cards', limit=150))
