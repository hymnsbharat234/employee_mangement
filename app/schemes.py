from pydantic import BaseModel, Field,EmailStr
from typing import Optional

class Employee(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    position: str = Field(..., min_length=1, max_length=100)
    salary: float = Field(..., gt=0)
    age: int = Field(..., ge=18, le=65)
    department: str = Field(..., min_length=1, max_length=100)

class EmployeeUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    position: Optional[str] = Field(None, min_length=1, max_length=100)
    salary: Optional[float] = Field(None, gt=0)
    age: Optional[int] = Field(None, ge=18, le=65)
    department: Optional[str] = Field(None, min_length=1, max_length=100)
