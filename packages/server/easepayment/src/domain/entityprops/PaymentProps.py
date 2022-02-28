from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import List


@dataclass
class PaymentProps:
    userId: str
    studentId: List[str]
    value: Decimal = 0.00
    created_at: datetime = None
    updated_at: datetime = None
