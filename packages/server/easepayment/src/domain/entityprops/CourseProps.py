import datetime
from dataclasses import dataclass


@dataclass
class CourseProps:
    name: str
    created_at: datetime = None
    updated_at: datetime = None
    state: bool = True
