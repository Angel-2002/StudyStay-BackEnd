from pydantic import BaseModel
from datetime import datetime

class Reservation(BaseModel):
    total_price : float
    stay_hours : int
    check_in_date : datetime
    check_out_date : datetime
    payment_method : str