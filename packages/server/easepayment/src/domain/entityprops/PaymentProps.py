from decimal import Decimal
from datetime import datetime
from dataclasses import dataclass


@dataclass
class PaymentProps:
    userId: str
    studentId: str
    value: Decimal = 0.00
    created_at: datetime = None
    updated_at: datetime = None
