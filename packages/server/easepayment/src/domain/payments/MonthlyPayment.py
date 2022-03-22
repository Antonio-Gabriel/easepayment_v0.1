from typing import List
from decimal import Decimal
from dataclasses import dataclass

from ..interfaces import IPayment


@dataclass
class MonthlyPaymentBase:
    studentId: List[str]
    userId: str
    value: Decimal
    month: str


class MonthlyPayment(IPayment):
    def __init__(self, month: str):
        self.month: str = month

    def payment_role(self, *args, **kwargs):
        """Rule for payment month"""

        return MonthlyPaymentBase(
            month=self.month,
            studentId=kwargs["studentId"],
            userId=kwargs["userId"],
            value=kwargs["value"],
        )
