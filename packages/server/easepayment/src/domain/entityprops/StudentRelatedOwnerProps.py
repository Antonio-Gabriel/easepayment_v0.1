from dataclasses import dataclass


@dataclass
class StudentRelatedOwnerProps:
    studentId: int
    ownerId: int
