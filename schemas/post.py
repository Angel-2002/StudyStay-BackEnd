from sqlalchemy import Column, Integer, String,Float
from database import Base

class PostS(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), unique=True, index=True)
    description = Column(String(300), unique=True, index=True)
    address = Column(String(100), unique=True, index=True)
    price = Column(Float, unique=True, index=True)
    rating = Column(Float, unique=True, index=True)
    image_url = Column(String(300), unique=True, index=True)
    nearest_universities = Column(String(300), unique=True, index=True)