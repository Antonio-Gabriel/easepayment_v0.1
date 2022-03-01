from typing import Type

from packages.server._shared.src.core.domain import IDomainEvents

from ..interfaces import IPayment


class PaymentBasedCreatedEvent(IDomainEvents):
    def __init__(self):
        self.__event_processed: any = None

    def dispatch(self, event: Type[any], payment_type: Type[IPayment]):
        """Dispatch payment based for using the last id"""

        payment_result = payment_type.payment_role(
            **{
                "userId": event.props.userId,
                "studentId": event.props.studentId,
                "value": event.props.value,
            }
        )

        self.__event_processed = payment_result

    def release_event(self):
        """Return event result"""

        return self.__event_processed
