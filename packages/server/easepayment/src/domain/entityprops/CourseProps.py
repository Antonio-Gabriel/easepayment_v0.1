import dataclasses
import datetime


@dataclasses
class CourseProps:
    name: str
    state: bool
    created_at: datetime
    updated_ap: datetime