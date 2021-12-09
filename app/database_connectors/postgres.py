import pandas
import psycopg2

from creds.cred_holder import Cred
from logs.logger.logger import Logger


class POSTGRESConnection:

    def __init__(self):
        self.info = Cred('postgres')
        self._logger = Logger(self)

    def __connect(self):
        self._logger.info('Opening the Connection')

        self._con = psycopg2.connect(
            host=self.info._host,
            user=self.info._user,
            password=self.info._password,
            dbname=self.info._database,
        )

        self._logger.info('Connection success')

        self._cur = self._con.cursor()

    def __disconnect(self):
        self._logger.info('Closing the Connection')

        self._con.close()

        self._logger.info('Connection close')

    def fetch(self, sql):
        self.__connect()
        self._cur.execute(sql)

        self._logger.info(f'run <<{sql}>>')

        result = self._cur.fetchall()
        self.__disconnect()
        return result

    def execute(self, sql):
        self.__connect()
        self._cur.execute(sql)
        self.__disconnect()

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
