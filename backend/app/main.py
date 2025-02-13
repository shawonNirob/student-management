from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.student_manual import router as student_router

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

@app.get("/")
def read_root():
    return {"message": "Welcome to Students FastAPI"}