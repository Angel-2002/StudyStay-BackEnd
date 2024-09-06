from pydantic import BaseModel
from typing import Optional

class User(BaseModel):

    full_name : str
    email  : str
    password : str
    phone : str
    image_url : Optional[str] = None
    role : Optional[str] = None