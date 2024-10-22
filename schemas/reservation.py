from sqlalchemy import Column, Integer, String,Float,DateTime
from database import Base

class ReservationS(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True, index=True)
    total_price = Column(Float, nullable=False, unique=False, index=True)
    stay_hours = Column(Integer, nullable=False, unique=False, index=True)
    check_in_date = Column(DateTime, nullable=False, unique=False, index=True)
    check_out_date = Column(DateTime, nullable=False, unique=False, index=True)
    payment_method = Column(String(100), nullable=False, unique=False, index=True)
    post_id = Column(Integer, nullable=False, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    
