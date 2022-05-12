from typing import List
from pydantic import BaseModel


class OwnerSchema(BaseModel):
    id: str
    name: str
    email: str
    phone: str

    class Config:
        orm_mode = True


class OwnerSchemaList(BaseModel):
    owners: List[OwnerSchema]


class OwnerSchemaRequest(BaseModel):
    name: str
    email: str
    phone: str


class OwnerRelatedStudentSchemaRequest(BaseModel):
    studentId: str
    ownerId: str

    class Config:
        orm_mode = True


class OwnerRelatedStudentBaseSchema(BaseModel):
    id: str
    process: int
    name: str
    email: str
    phone: str
    classe_name: str
    course_name: str

    class Config:
        orm_mode = True


class OwnerRelatedStudentSchema(BaseModel):
    students: List[OwnerRelatedStudentBaseSchema]
