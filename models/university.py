from pydantic import BaseModel

class University(BaseModel):
    logourl:str
    name:str
    initials:str
    sedes:str
    type:str
