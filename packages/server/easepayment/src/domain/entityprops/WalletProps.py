import datetime
from decimal import Decimal
from dataclasses import dataclass


@dataclass
class WallerProps:
    userId: int
    balance: Decimal = 0.00
    created_at: datetime = None
    updated_at: datetime = None
