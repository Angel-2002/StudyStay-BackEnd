from pydantic import BaseModel

class Alumno(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True