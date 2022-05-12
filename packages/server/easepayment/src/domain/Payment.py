from uuid import uuid4
from dataclasses import dataclass

from datetime import datetime
from .entityprops import PaymentProps

from packages.server._shared.src.core.logic import Result
from packages.server._shared.src.core.domain import Entity


@dataclass
class PaymentPropsResult(PaymentProps):
    id: str = None


class Payment:
    class __private(Entity[PaymentProps]):
        def __init__(
            self,
            props: PaymentProps,
            id: str = None,
        ):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: PaymentProps, id: str = None):
        """create Payment object"""

        if not id:
            id = uuid4()

        if props.value == 0.00:
            Result.fail("report a true price from pay")

        props.created_at = datetime.now()
        props.updated_at = datetime.now()

        payment = cls.__private(props, id)

        return Result.ok(
            PaymentPropsResult(
                id=id,
                userId=payment.props.userId,
                studentId=payment.props.studentId,
                value=payment.props.value,
                created_at=payment.props.created_at,
                updated_at=payment.props.updated_at,
            )
        )
