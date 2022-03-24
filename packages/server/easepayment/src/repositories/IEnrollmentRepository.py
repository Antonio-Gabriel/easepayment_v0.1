from abc import ABC, abstractmethod
from ..domain.entityprops import EnrollmentProps


class IEnrollmentRepository(ABC):
    @abstractmethod
    def save(enrollment_props: EnrollmentProps):
        """Save enrollment into db"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def delete(class_related_course_id: str, student_id: str):
        """Delete enrollment"""

        raise NotImplementedError("Method not implemented")
