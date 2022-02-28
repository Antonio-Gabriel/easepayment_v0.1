from dataclasses import dataclass

from packages.server.easepayment.src.domain.enums import Months


@dataclass
class MonthlyPaymentProps:
    month: Months
    paymentId: int
    studentId: int
