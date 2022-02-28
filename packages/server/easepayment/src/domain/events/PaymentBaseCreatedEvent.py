from typing import Type
from packages.server._shared.src.core.domain.events.IDomainEvent import IDomainEvent

from ..interfaces import IPayment


class PaymentBasedCreatedEvent(IDomainEvent):

    __event_processed: any = None

    def dispatch(event: Type[any], payment_type: Type[IPayment]):
        """Dispatch payment based for using the last id"""

        payment_result = payment_type.payment_role(
            **{
                "userId": event.props.userId,
                "studentId": event.props.studentId,
                "value": event.props.value,
            }
        )

        PaymentBasedCreatedEvent.__event_processed = payment_result

    @staticmethod
    def release_event():
        """Return event result"""

        return PaymentBasedCreatedEvent.__event_processed
