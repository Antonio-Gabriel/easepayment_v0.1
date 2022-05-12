from abc import ABC, abstractmethod
from ..domain.entityprops import ClassRelatedCourseProps


class IClasseRelatedCourseRepository(ABC):
    @abstractmethod
    def save(related_props: ClassRelatedCourseProps):
        """Save classe related course with student"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_class_with_courses():
        """Get all classes with respective courses"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def delete(id: str):
        """delete classe related course with student"""

        raise NotImplementedError("Method not implemented")
