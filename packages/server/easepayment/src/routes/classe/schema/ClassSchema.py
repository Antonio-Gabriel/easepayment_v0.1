from typing import List
from pydantic import BaseModel


class ClassSchema(BaseModel):
    id: str
    classe_id: str
    course_id: str
    price: float

    class Config:
        orm_mode = True


class ClassRelatedCourseSchema(BaseModel):
    id: str
    name: str
    classe_name: str
    price: float

    class Config:
        orm_mode = True


class ClassSchemaList(BaseModel):
    courses: List[ClassRelatedCourseSchema]


class ClassSchemaRequest(BaseModel):
    classe_id: str
    course_id: str
    price: float
