from abc import ABC, abstractmethod
from ..domain.entityprops import ClassRelatedCourseProps


class IClasseRelatedCourseRepository(ABC):
    @abstractmethod
    def save(related_props: ClassRelatedCourseProps):
        """Save classe related course with student"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def delete(related_props: ClassRelatedCourseProps):
        """delete classe related course with student"""

        raise NotImplementedError("Method not implemented")
