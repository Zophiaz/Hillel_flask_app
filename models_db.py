from sqlalchemy import Column, Integer, String, Float
from alchemy_db import Base


class SQL_base(Base):
    __tablename__ = 'currency'
    id = Column(Integer, primary_key=True, unique=True)
    bank = Column(String(20))
    currency = Column(String(10))
    date_exchange = Column(String(10))
    buy_rate = Column(Float)
    sale_rate = Column(Float)

    def __init__(self, bank, currency, date_exchange, buy_rate, sale_rate):
        self.bank = bank
        self.currency = currency
        self.date_exchange = date_exchange
        self.buy_rate = buy_rate
        self.sale_rate = sale_rate

    def __repr__(self):
        return f'<User {self.name!r}>'
