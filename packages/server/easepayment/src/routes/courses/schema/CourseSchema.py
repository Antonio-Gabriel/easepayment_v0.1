from typing import List
from datetime import datetime
from pydantic import BaseModel


class CourseSchema(BaseModel):
    id: str
    name: str
    state: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class CourseSchemaList(BaseModel):
    courses: List[CourseSchema]


class CourseSchemaRequest(BaseModel):
    name: str


class CourseSchemaRequestUpdate(BaseModel):
    name: str
    state: bool
