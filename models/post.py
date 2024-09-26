from pydantic import BaseModel

class Post(BaseModel):
    title : str
    description : str
    address : str
    price : float
    rating  : float
    image_url : str
    nearest_universities : str
    userid: int