from sqlalchemy import Column, Integer, String
from database import Base

class UserS(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(100), unique=True, index=True)
    phone = Column(String(20), unique=True, index=True)
    image_url = Column(String(300), nullable=True, index=True)
    role = Column(String(100), nullable=True, index=True)