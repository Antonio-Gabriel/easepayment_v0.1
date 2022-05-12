from pydantic import BaseModel


class AccountSchemaResponse(BaseModel):
    id: str
    username: str
    password: str


class AccountSchemaRequest(BaseModel):
    username: str
    password: str


class AccountSchemaUpdateRequest(BaseModel):
    username: str
    password: str
    currentPassword: str
