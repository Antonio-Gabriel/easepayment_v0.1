import datetime
from dataclasses import dataclass


@dataclass
class EnrollmentProps:
    class_related_course_id: str
    student_id: str
    created_at: datetime = None
    updated_at: datetime = None
