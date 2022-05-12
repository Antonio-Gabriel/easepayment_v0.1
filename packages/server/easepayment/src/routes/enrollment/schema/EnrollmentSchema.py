from typing import List
from datetime import datetime
from pydantic import BaseModel


class EnrollmentSchema(BaseModel):
    class_related_course_id: str
    student_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class EnrollmentSchemaList(BaseModel):
    enrollments: List[EnrollmentSchema]


class EnrollmentSchemaRequest(BaseModel):
    class_related_course_id: str
    student_id: str
