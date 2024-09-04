from sqlalchemy import Column, Integer, String
from database import Base

class UniversityS(Base):
    __tablename__ = 'universities'

    id = Column(Integer, primary_key=True, index=True)
    logourl = Column(String(300), unique=True, index=True)
    name = Column(String(100), unique=True, index=True)
    initials = Column(String(10), unique=True, index=True)
