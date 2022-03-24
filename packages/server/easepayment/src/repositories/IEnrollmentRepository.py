from abc import ABC, abstractmethod
from ..domain.entityprops import EnrollmentProps


class IEnrollmentRepository(ABC):
    @abstractmethod
    def save(enrollment_props: EnrollmentProps):
        """Save enrollment into db"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def delete(enrollment_props: EnrollmentProps):
        """Delete enrollment"""

        raise NotImplementedError("Method not implemented")
