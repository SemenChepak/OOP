from sqlalchemy import Integer, Column, Date, String, ForeignKey, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class People(Base):
    __tablename__ = 'people'
    id_code = Column(Integer, unique=True, primary_key=True, nullable=False)
    customer_id = Column(String(100), unique=True, nullable=False)
    name = Column(String(32), nullable=False)
    second_name = Column(String(32))
    surname = Column(String(32), nullable=False)
    phone = Column(String(50), nullable=False)
    city = Column(String(32), nullable=False)
    birth_date = Column(Date(), nullable=False)


class Cards(Base):
    __tablename__ = 'cards'
    card_id = Column(String(100), unique=True, primary_key=True)
    holder_id = Column(String(100),
                       ForeignKey(People.customer_id), nullable=False)
    card_no = Column(String(16), unique=True, nullable=False)
    valid_until = Column(String(256))
    created_on = Column(String(256))
    last_used_on = Column(String(256))
    currency = Column(String(32), nullable=False)
    amount = Column(FLOAT, nullable=False)


class Transactions(Base):
    __tablename__ = 'transactions'
    transaction_id = Column(String(100), primary_key=True, unique=True, )
    card_number = Column(String(16), ForeignKey(Cards.card_no), nullable=False)
    transaction_time = Column(String(256))
    comment = Column(String(256))
    value = Column(FLOAT)
