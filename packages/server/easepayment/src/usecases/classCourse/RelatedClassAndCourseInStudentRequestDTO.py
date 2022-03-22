from decimal import Decimal
from dataclasses import dataclass, fields


@dataclass
class RelatedClassAndCourseInStudentRequestDTO:
    classId: str
    courseId: str
    studentId: str
    price: Decimal = 0.00

    def __post_init__(self):
        """Initialize the object"""

        for field in fields(self):
            value = getattr(self, field.name)
            if not isinstance(value, field.type):
                raise ValueError(
                    f"Expected {field.name} to be of type {field.type}, got {repr(value)}"
                )
