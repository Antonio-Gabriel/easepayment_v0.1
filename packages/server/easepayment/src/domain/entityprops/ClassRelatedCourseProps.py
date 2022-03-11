from dataclasses import dataclass
from decimal import Decimal


@dataclass
class ClassRelatedCourseProps:
    classId: str
    courseId: str
    studentId: str
    price: Decimal = 0.00
