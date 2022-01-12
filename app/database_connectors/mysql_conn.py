import pandas
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from creds.cred_holder import Cred
from database_connectors.db_models.models import People, Cards, Transactions
from logs.logger.logger import Logger


class MSQLConnector:

    def __init__(self):
        self.info = Cred('mysql')
        self._logger = Logger(self)
        self.engine = create_engine(self.__engine)
        self.Session = sessionmaker(bind=self.engine)

    def select_people(self):
        with self.Session() as sess:
            res = sess.query(
                People.id_code,
                People.customer_id,
                People.name,
                People.second_name,
                People.surname,
                People.phone,
                People.city,
                People.birth_date
            ).all()

            return self.change_type(res)

    def select_cards(self):
        with self.Session() as sess:
            res = sess.query(
                Cards.card_id,
                Cards.holder_id,
                Cards.card_no,
                Cards.valid_until,
                Cards.created_on,
                Cards.last_used_on,
                Cards.currency,
                Cards.amount
            ).all()
            return res

    def select_transactions(self):
        with self.Session() as sess:
            res = sess.query(
                Transactions.transaction_id,
                Transactions.card_number,
                Transactions.transaction_time,
                Transactions.comment,
                Transactions.value
            ).all()
            return res

    def write_to_mysql(self, data_frame, table_name: str):
        self._logger.info('start uploading file')
        pandas.DataFrame(data_frame). \
            to_sql(
            con=self.__engine,
            name=table_name,
            if_exists='replace'
        )

    @property
    def __engine(self):
        return self.info._uri

    @staticmethod
    def change_type(df):
        ex = []
        for row in df:
            ex.append(dict(row))
        return ex


a = MSQLConnector()
res = a.select_people()
print(a.change_type(res))
