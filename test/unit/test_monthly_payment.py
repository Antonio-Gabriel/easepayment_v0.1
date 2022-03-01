from unittest import TestCase
from uuid import uuid4

from packages.server.easepayment.src.domain import Payment
from packages.server.easepayment.src.domain.payments import MonthlyPayment
from packages.server.easepayment.src.domain.entityprops import PaymentProps


class TestMonthlyPaymentEntity(TestCase):
    def test_monthly_payment(self):

        payment = Payment.create(
            PaymentProps(
                userId=uuid4(),
                studentId=[uuid4(), uuid4()],
                value=12000
            ),
            MonthlyPayment(
                month="Janeiro"
            ),
        )
        print(payment)
        # print(payment.get_value())
        # print("oi")

        self.assertTrue(True)
