from sqlalchemy import Column, Integer, String,Float
from database import Base

class PostS(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False, unique=False, index=True)
    description = Column(String(300), nullable=False, unique=False, index=True)
    address = Column(String(100), nullable=False, unique=True, index=True)
    price = Column(Float, nullable=False, unique=False, index=True)
    rating = Column(Float, nullable=False, unique=False, index=True)
    image_url = Column(String(300), nullable=False, unique=False, index=True)
    nearest_universities = Column(String(300), nullable=False, unique=False, index=True)