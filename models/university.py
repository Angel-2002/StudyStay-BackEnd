from pydantic import BaseModel

class University(BaseModel):
    logourl:str
    name:str
    initials:str
