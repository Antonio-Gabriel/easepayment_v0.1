from abc import ABC, abstractmethod

from click import DateTime


class IDomainEvent(ABC):
    """Usecase interface"""

    date_time_occurred: DateTime = None

    @abstractmethod
    def get_aggregate_id() -> int:
        raise NotImplementedError("Method not implemented")
