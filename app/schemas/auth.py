from pydantic import BaseModel, Field,EmailStr
from typing import Optional

class UserRegister(BaseModel):
    username: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6)
class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)