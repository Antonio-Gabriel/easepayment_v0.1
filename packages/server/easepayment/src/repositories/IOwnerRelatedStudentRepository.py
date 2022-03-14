from abc import ABC, abstractmethod
from ..domain.entityprops import StudentRelatedOwnerProps


class IOwnerRelatedStudentRepository(ABC):
    @abstractmethod
    def save(related_props: StudentRelatedOwnerProps):
        """Save stutend related owner into db"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def find_related_student(owner_id: str, student_id: str):
        """Find related student"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def delete(related_props: StudentRelatedOwnerProps):
        """delete stutend related owner into db"""

        raise NotImplementedError("Method not implemented")
