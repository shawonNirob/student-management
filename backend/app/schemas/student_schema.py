from pydantic import BaseModel
from typing import Optional

class StudentBase(BaseModel):
    student_id: int
    university_name: Optional[str] = None
    contact_number: str  
    email: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    name: Optional[str] = None
    department: Optional[str] = None
    batch_year: Optional[int] = None
    level: Optional[str] = None

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    university_name: Optional[str] = None
    contact_number: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    name: Optional[str] = None
    department: Optional[str] = None
    batch_year: Optional[int] = None
    level: Optional[str] = None

class StudentResponse(StudentBase):
    class Config:
        from_attributes = True