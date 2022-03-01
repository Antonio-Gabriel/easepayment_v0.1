from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserProps:
    accountId: str
    ownerId: str
    studentId: str
    created_at: datetime = None
    updated_at: datetime = None
    state: bool = True
