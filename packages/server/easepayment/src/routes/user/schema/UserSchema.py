from typing import List
from datetime import datetime
from pydantic import BaseModel


class UserSchemaResponse(BaseModel):
    id: str
    account_id: str
    owner_id: str
    state: bool
    created_at: datetime
    updated_at: datetime


class UserSchemaFilterResponse(BaseModel):
    id: str
    name: str
    username: str
    email: str
    phone: str
    created_at: datetime
    updated_at: datetime


class UserSchemaFilter(BaseModel):
    user: List[UserSchemaFilterResponse]


class UserSchemaRequest(BaseModel):
    account_id: str
    owner_id: str = None
    student_id: str = None
    state: bool
