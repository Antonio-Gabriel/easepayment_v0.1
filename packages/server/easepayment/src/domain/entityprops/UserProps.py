from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserProps:
    account_id: any
    owner_id: any
    student_id: any
    created_at: datetime = None
    updated_at: datetime = None
    state: bool = True
