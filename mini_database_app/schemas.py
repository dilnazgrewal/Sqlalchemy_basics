# schemas.py
from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    age: int
    email: str

class StudentOut(BaseModel):
    id: int
    name: str
    age: int
    email: str
    class Config:
        from_attributes = True   # lets Pydantic read SQLAlchemy objects directly

class CourseCreate(BaseModel):
    name: str

class CourseOut(BaseModel):
    id: int
    name: str
    class Config:
        from_attributes = True   # lets Pydantic read SQLAlchemy objects directly