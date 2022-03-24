from dataclasses import dataclass


@dataclass
class ClassRelatedCourseProps:
    classId: str
    courseId: str
    price: float = 0.00
