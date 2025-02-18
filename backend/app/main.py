from fastapi import FastAPI
from sqlalchemy.sql import text
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.student_manual import router as student_router
from app.api.routes.student_AI import router as student_AI_router
from app.db import get_db, engine, Base
from app.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student_router, prefix="/students", tags=["students"])
app.include_router(student_AI_router, prefix="/ai", tags=["ai"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Students FastAPI"}

@app.get("/_status")
def status():
    return {"status": "ok"}

@app.get("/_db_status")
def db_status():
    try:
        db = next(get_db())
        db.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

