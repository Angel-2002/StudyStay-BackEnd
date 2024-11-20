from pydantic import BaseModel, Field
from typing import Optional

class Card(BaseModel):

    userid : int
    name : str
    logo_url : Optional[str] = Field(default="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Old_Visa_Logo.svg/1200px-Old_Visa_Logo.svg.png")
    name_holder : str
    number_card : str
    cvv : str
    month : str
    year : str