from fastapi import APIRouter, HTTPException, Depends
from app.db import get_db
from app.schemas.ask_schema import AskRequest
from app.crud.student_AI_crud import process_llm_query

router = APIRouter()

@router.post("/ask", response_model=dict, status_code=200)
def ask(request: AskRequest, db=Depends(get_db)):
    try:
        return process_llm_query(db, request.query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
