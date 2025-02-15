from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from app.db import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, unique=True, nullable=False)
    university_name = Column(String(250), nullable=True)
    contact_number = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=True)
    age = Column(Integer, nullable=True)
    gender = Column(String(50), nullable=True)
    name = Column(String(100), nullable=True)
    department = Column(String(150), nullable=True)
    batch_year = Column(Integer, nullable=True)
    level = Column(String(50), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())