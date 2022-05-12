from ..sqlAlchemy import engine, payment

from ...repositories import IPaymentRepo


class PaymentRepository(IPaymentRepo):
    def pay(user_id: str, student_id: str, amount: float, pay_id: str):
        """Pay"""
        connection = engine.connect()
        statement = payment.insert()
        result = connection.execute(
            statement,
            {
                "id": pay_id,
                "user_id": user_id,
                "student_id": student_id,
                "amount": amount,
            },
        )

        if result:
            return pay_id
