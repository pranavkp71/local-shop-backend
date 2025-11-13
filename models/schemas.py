from pydantic import BaseModel
from typing import Optional

class Shops(BaseModel):
    name: str
    category_id: str
    description: Optional[str]
    address: str
    image_url: Optional[str] = None

class Categories(BaseModel):
    name: str

class Area(BaseModel):
    name: str

class Admin(BaseModel):
    email: str
    password: str
    

