from sqlalchemy.sql import select
from ..sqlAlchemy import engine, monthly_payment, payment, user

from ...repositories import IMonthlyRepository


class MonthlyRepository(IMonthlyRepository):
    def pay_month(id: str, pay_id: str, month: str):
        """Save monthly"""
        connection = engine.connect()
        statement = monthly_payment.insert()
        result = connection.execute(
            statement,
            {
                "id": id,
                "month": month,
                "payment_id": pay_id,
            },
        )

        return result

    def find_montly_payed(user_id: str, month: str):
        """Find monthly payed"""
        connection = engine.connect()
        query = (
            select([monthly_payment.c.month])
            .select_from(
                monthly_payment.outerjoin(
                    payment, monthly_payment.c.payment_id == payment.c.id
                )
            )
            .where(monthly_payment.c.month == month, payment.c.user_id == user_id)
        )
        result = connection.execute(query)

        row = result.fetchone()

        result.close()

        return row

    def get_monthly_payed(user_id: str):
        """Get monthly payed"""
        connection = engine.connect()
        query = (
            select(
                [
                    payment.c.id,
                    monthly_payment.c.month,
                    payment.c.student_id,
                    payment.c.amount,
                ]
            )
            .select_from(
                payment.outerjoin(user, payment.c.user_id == user.c.id).outerjoin(
                    monthly_payment, monthly_payment.c.payment_id == payment.c.id
                )
            )
            .where(payment.c.user_id == user_id, monthly_payment.c.month != None)
        )

        result = connection.execute(query).fetchall()

        return result
