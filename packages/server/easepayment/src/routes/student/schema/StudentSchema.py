from typing import List
from pydantic import BaseModel


class StudentSchema(BaseModel):
    id: str
    name: str
    email: str
    phone: str
    process: int
    district: str
    location: str

    class Config:
        orm_mode = True


class StudentAutoRelatedSchema(BaseModel):
    owner_studentId: str
    studentId: str

    class Config:
        orm_mode = True


class StudentAutoRelatedSchemaResponse(BaseModel):
    owner_studentId: str
    studentId: str

    class Config:
        orm_mode = True


class StudentSchemaList(BaseModel):
    students: List[StudentSchema]


class StudentSchemaRequest(BaseModel):
    name: str
    email: str
    phone: str
    process: int
    district: str
    location: str
