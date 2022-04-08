from abc import ABC, abstractmethod
from ..domain.entityprops import StudentProps


class IStudentAutoRelated(ABC):
    @abstractmethod
    def save(owner_student_id: str, student_id: str):
        """Save stutend related owner into db"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def find_related_student(owner_student_id: str, student_id: str):
        """Find related student"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def unrelated(owner_student_id: str, student_id: str):
        """Unrelated student into db"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def delete(related_props: StudentProps):
        """delete stutend related owner into db"""

        raise NotImplementedError("Method not implemented")
