from sqlalchemy import Column, Integer, String,Float,DateTime
from database import Base

class ReservationS(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True, index=True)
    total_price = Column(Float, unique=True, index=True)
    stay_hours = Column(Integer, unique=True, index=True)
    check_in_date = Column(DateTime, unique=True, index=True)
    check_out_date = Column(DateTime, unique=True, index=True)
    payment_method = Column(String(100), unique=True, index=True)
