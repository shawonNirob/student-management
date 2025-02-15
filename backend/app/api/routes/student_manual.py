from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List

from app.db import get_db
from app.schemas.student_schema import StudentCreate, StudentUpdate, StudentResponse
from app.crud.student_crud import (
    create_student, get_students, get_student_by_id,
    update_student, delete_student, get_student_by_contact
)

router = APIRouter()

@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_new_student(student: StudentCreate, db: Session = Depends(get_db)):
    try:
        existing_student = get_student_by_id(db, student.student_id)
        if existing_student:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Student with this ID already exists"
            )

        return create_student(db, student)
    
    except IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Duplicate entry detected: Student ID or Contact Number already exists."
        )

@router.get("/", response_model=dict, status_code=status.HTTP_200_OK)
def fetch_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students, total_count = get_students(db, skip, limit)
    return {
        "students": [StudentResponse.from_orm(student) for student in students],
        "total_count": total_count
    }

@router.get("/{student_id}", response_model=StudentResponse, status_code=status.HTTP_200_OK)
def fetch_student_by_id(student_id: int, db: Session = Depends(get_db)):
    student = get_student_by_id(db, student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    return student

@router.get("/contact/{contact_number}", response_model=StudentResponse, status_code=status.HTTP_200_OK)
def fetch_student_by_contact_number(contact_number: str, db: Session = Depends(get_db)):
    student = get_student_by_contact(db, contact_number)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    return student

@router.put("/{student_id}", response_model=StudentResponse, status_code=status.HTTP_200_OK)
def modify_student(student_id: int, student: StudentUpdate, db: Session = Depends(get_db)):
    updated_student = update_student(db, student_id, student)
    if not updated_student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    return updated_student

@router.delete("/{student_id}", status_code=status.HTTP_200_OK)
def remove_student(student_id: int, db: Session = Depends(get_db)):
    deleted_student = delete_student(db, student_id)
    if not deleted_student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    return {"message": "Student deleted successfully"}