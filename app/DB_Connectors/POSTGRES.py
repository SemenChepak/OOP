import psycopg2
import pandas

from creds.CRED_holder import Cred
from logs.Logger.Loger import DataLogger

class PostgresConnector:

    def __init__(self):
        self.info = Cred('postgres')
        self._logger = DataLogger(self)

    def __connect__(self):
        self._logger.warn('Opening the Connection')

        self._con = psycopg2.connect(
            host=self.info._host,
            user=self.info._user,
            password=self.info._password,
            dbname=self.info._database,
        )

        self._logger.warn('Connection success')

        self._cur = self._con.cursor()

    def __disconnect__(self):
        self._logger.warn('Closing the Connection')

        self._con.close()

        self._logger.warn('Connection close')

    def fetch(self, sql):
        self.__connect__()
        self._cur.execute(sql)

        self._logger.info(f'run <<{sql}>>')

        result = self._cur.fetchall()
        self.__disconnect__()
        return result

    def execute(self, sql):
        self.__connect__()
        self._cur.execute(sql)
        self.__disconnect__()

    @property
    def __engine(self):
        return f'postgresql://{self.info._user}:' \
               f'{self.info._password}@' \
               f'{self.info._host}/' \
               f'{self.info._database}'

    def write_to_postgres(self, data_frame, table_name: str):
        pandas.DataFrame(data_frame). \
            to_sql(
            con=self.__engine,
            name=table_name,
            if_exists='replace'
        )