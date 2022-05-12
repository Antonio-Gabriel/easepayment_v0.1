from sqlalchemy.sql import select
from ..sqlAlchemy import engine, uniform_type, uniform_payment, user, payment
from ...repositories import IUniformRepository


class UniformRepository(IUniformRepository):
    def pay_uniform(id: str, uniform_type_id: str, payment_id: str):
        """Pay uniform"""

        connection = engine.connect()
        statement = uniform_payment.insert()

        result = connection.execute(
            statement,
            {
                "id": id,
                "uniform_type_id": uniform_type_id,
                "payment_id": payment_id,
            },
        )

        return result

    def save_uniform_type(id: str, type: str, price: float):
        """Save uniform type"""
        connection = engine.connect()
        statement = uniform_type.insert()

        result = connection.execute(
            statement,
            {
                "id": id,
                "type": type,
                "price": price,
            },
        )

        return result

    def get_uniform_type():
        """Uniform type"""
        connection = engine.connect()
        query = select(uniform_type)
        result = connection.execute(query)

        row = result.fetchall()

        result.close()

        return row

    def get_uniform_payed(user_id: str):
        """Get uniform payed"""

        connection = engine.connect()
        query = (
            select(
                [
                    payment.c.id,
                    uniform_type.c.type,
                    uniform_type.c.price,
                    payment.c.student_id,
                    payment.c.amount,
                ]
            )
            .select_from(
                payment.outerjoin(user, payment.c.user_id == user.c.id)
                .outerjoin(
                    uniform_payment, uniform_payment.c.payment_id == payment.c.id
                )
                .outerjoin(
                    uniform_type, uniform_type.c.id == uniform_payment.c.uniform_type_id
                )
            )
            .where(payment.c.user_id == user_id, uniform_type.c.type != None)
        )

        result = connection.execute(query).fetchall()

        return result
