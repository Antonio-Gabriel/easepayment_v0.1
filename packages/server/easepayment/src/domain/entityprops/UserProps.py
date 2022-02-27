
from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserProps:
    accountId: int
    ownerId: int
    studentId: int
    created_at: datetime = None
    updated_at: datetime = None
    state: bool = True  