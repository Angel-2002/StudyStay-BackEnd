from sqlalchemy import Column, Integer, String
from database import Base

class CardS(Base):
    __tablename__ = 'credit_card'

    id = Column(Integer, primary_key=True, index=True)
    userid = Column(Integer, nullable=False, index=True)
    name = Column(String(300), nullable=False, unique=False, index=True)
    logo_url = Column(String(300), nullable=False, unique=False, index=True)
    name_holder = Column(String(300), nullable=False, unique=False, index=True)
    number_card = Column(String(16), nullable=False, unique=False, index=True)
    cvv = Column(String(3), nullable=False, unique=False, index=True)
    month = Column(String(2), nullable=False, unique=False, index=True)
    year = Column(String(4), nullable=False, unique=False, index=True)