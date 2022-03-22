from decimal import Decimal
from dataclasses import dataclass


@dataclass
class ClassRelatedCourseProps:
    classId: str
    courseId: str
    studentId: str
    price: Decimal = 0.00
