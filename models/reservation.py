from pydantic import BaseModel

class Reservation(BaseModel):
    total_price : float
    stay_hours : int
    check_in_date : str
    check_out_date : str
    payment_method : str
    post_id: int
    user_id: int