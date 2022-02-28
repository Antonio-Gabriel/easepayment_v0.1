from dataclasses import dataclass
from decimal import Decimal


@dataclass
class ClassRelatedCourseProps:
    classId: str
    courseId: str
    price: Decimal = 0.00
