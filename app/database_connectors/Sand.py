a = 'mysql+mysqlconnector://root:1111@localhost:3306/sqlalchemy'
from sqlalchemy import Integer, Column, Date, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

ENG = create_engine(a)
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


from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=ENG)
ses = Session()
res = ses.query(People).all()
for i in res:
    print(i)
