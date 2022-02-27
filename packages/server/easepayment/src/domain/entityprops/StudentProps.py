from dataclasses import dataclass
from .ClassRelatedCourseProps import ClassRelatedCourseProps


@dataclass
class StudentProps:
    name: str
    process: int
    email: str
    phone: str
    district: str
    location: str
    avatar: str
    classCourse: ClassRelatedCourseProps
    state: bool = True
