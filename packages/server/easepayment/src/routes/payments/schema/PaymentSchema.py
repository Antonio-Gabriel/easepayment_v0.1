from pydantic import BaseModel


class PaymentSchema(BaseModel):
    userId: str
    studentId: str
    month: str
    value: float


class UniformTypeSchema(BaseModel):
    type: str
    price: float


class UniformPaymentSchema(BaseModel):
    uniform_type_type: str
    amount: float
    userId: str
    studentId: str
