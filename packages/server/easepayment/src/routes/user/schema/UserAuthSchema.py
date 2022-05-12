from pydantic import BaseModel


class UserAuthSchema(BaseModel):
    email: str
    password: str
