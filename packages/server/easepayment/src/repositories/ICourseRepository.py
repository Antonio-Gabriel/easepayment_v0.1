from abc import ABC, abstractmethod

from ..domain.entityprops import CourseProps


class ICourseRepository(ABC):
    @abstractmethod
    def save(course_props: CourseProps):
        """Save course"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def find_course(name: str):
        """Find course"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def delete(courseId: str):
        """delete course"""

        raise NotImplementedError("Method not implemented")
