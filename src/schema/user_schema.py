from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    name: str
    email: str
    password: str
    perfilImage: Optional[str]


    class Config:
        orm_mode = True
