from datetime import datetime
from typing import Type
from packages.server._shared.src.core.domain import Entity
from packages.server._shared.src.core.logic import Result

from uuid import uuid4

from .interfaces import IPayment
from .entityprops import PaymentProps
from .events import PaymentBasedCreatedEvent


class Payment:
    class __private(Entity[PaymentProps]):
        def __init__(
            self,
            props: PaymentProps,
            id: Type[uuid4] = None,
        ):
            super().__init__(props, id)

    @classmethod
    def create(
        cls, props: PaymentProps, payment_type: Type[IPayment], id: Type[uuid4] = None
    ):
        """create Payment object"""

        if not id:
            id = uuid4()

        if props.value == 0.00:
            Result.fail("report a true price from pay")

        props.created_at = datetime.now()
        props.updated_at = datetime.now()

        payment = cls.__private(props, id)

        PaymentBasedCreatedEvent.dispatch(payment, payment_type)

        return Result.ok(payment.props)
