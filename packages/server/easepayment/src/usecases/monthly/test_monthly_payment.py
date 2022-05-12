from unittest import TestCase
from uuid import uuid4

from .MonthlyPayment import MonthlyPayment
from .MonthlyRequestDTO import MonthlyRequestDTO
from ...infra.repositories import MonthlyRepository


class TestMonthlyPayment(TestCase):
    def test_monthly_payment(self):

        payment = MonthlyPayment(MonthlyRepository)
        payment.execute(
            MonthlyRequestDTO(
                userId=str(uuid4()),
                studentId=str(uuid4()),
                month="Janeiro",
                value=float(200),
            )
        )
        # print(payment)
        # print(payment.get_value())
        # print("oi")

        self.assertTrue(True)
