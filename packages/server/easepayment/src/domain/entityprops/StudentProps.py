from dataclasses import dataclass


@dataclass
class StudentProps:
    name: str
    process: int
    email: str
    phone: str
    district: str
    location: str
    avatar: str
    state: bool = True
