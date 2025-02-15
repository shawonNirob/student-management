from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student_schema import StudentCreate, StudentUpdate

def create_student(db: Session, student: StudentCreate):
    new_student = Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

def get_students(db: Session, skip: int = 0, limit: int = 10):
    students = db.query(Student).offset(skip).limit(limit).all()
    total_count = db.query(Student).count()
    return students, total_count

def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(Student.student_id == student_id).first()

def get_student_by_contact(db: Session, contact_number: int): 
    return db.query(Student).filter(Student.contact_number == contact_number).first()

def update_student(db: Session, student_id: int, student: StudentUpdate):
    db_student = db.query(Student).filter(Student.student_id == student_id).first()
    if db_student:
        for key, value in student.dict(exclude_unset=True).items():
            setattr(db_student, key, value)
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = db.query(Student).filter(Student.student_id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student