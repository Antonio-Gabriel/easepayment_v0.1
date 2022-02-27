from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class PaymentProps:
    userId: int
    value: Decimal = 0.00
    created_at: datetime = None
    updated_at: datetime = None
