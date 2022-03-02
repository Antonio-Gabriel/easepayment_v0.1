from dataclasses import dataclass


@dataclass
class UserRequestDTO:
    account_id: any
    owner_id: any
    student_id: any
    state: bool
