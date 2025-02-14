from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from app.db import Base

class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True,nullable=False)
    university_name = Column(String(250), nullable=True)
    contact_number = Column(String(50), unique_key=True, nullable=False)
    age = Column(Integer, nullable=True)
    gender = Column(String(50), nullable=True)
    name = Column(String(100), nullable=True)
    department = Column(String(150), nullable=True)
    batch_year = Column(Integer, nullable=True)
    level = Column(String(50), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())