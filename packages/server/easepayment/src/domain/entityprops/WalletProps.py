
from dataclasses import dataclass
import datetime
from decimal import Decimal


@dataclass
class WallerProps:
    userId: int
    balance: Decimal = 0.00
    created_at: datetime = None
    updated_at: datetime = None