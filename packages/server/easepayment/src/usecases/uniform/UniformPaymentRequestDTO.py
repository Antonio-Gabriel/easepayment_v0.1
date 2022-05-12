from dataclasses import dataclass


@dataclass
class UniformPaymentRequestDTO:
    uniform_type_type: str
    amount: float
    userId: str
    studentId: str
