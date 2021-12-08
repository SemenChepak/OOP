import pymysql
import pandas

from creds.CRED_holder import Cred


class MYSQLConnector:

    def __init__(self):
        self.info = Cred('mysql')

    def __connect__(self):
        self._con = pymysql.connect(
            host=self.info._host,
            user=self.info._user,
            password=self.info._password,
            db=self.info._database,
            cursorclass=pymysql.cursors.DictCursor
        )
        self._cur = self._con.cursor()

    def __disconnect__(self):
        self._con.close()

    def fetch(self, sql):
        self.__connect__()
        self._cur.execute(sql)
        result = self._cur.fetchall()
        self.__disconnect__()
        return result

    def execute(self, sql):
        self.__connect__()
        self._cur.execute(sql)
        self.__disconnect__()

    def write_to_mysql(self, data_frame, table_name: str):
        pandas.DataFrame(data_frame). \
            to_sql(
            con=self.__engine,
            name=table_name,
            if_exists='replace'
        )

    @property
    def __engine(self):
        return f'mysql+mysqlconnector://{self.info._user}:' \
               f'{self.info._password}@' \
               f'{self.info._host}/' \
               f'{self.info._database}'



