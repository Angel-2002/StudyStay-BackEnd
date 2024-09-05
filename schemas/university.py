from sqlalchemy import Column, Integer, String
from database import Base

class UniversityS(Base):
    __tablename__ = 'universities'

    id = Column(Integer, primary_key=True, index=True)
    logourl = Column(String(300), nullable=False, unique=True, index=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    initials = Column(String(10), nullable=False, unique=True, index=True)
    sedes = Column(String(100), nullable=False, unique=False, index=True)
    type = Column(String(30), nullable=False, unique=False, index=True)
