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
    def update(course_props: CourseProps):
        """update course"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get():
        """get all course"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_by_id(course_id: str):
        """get course by id"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def delete(courseId: str):
        """delete course"""

        raise NotImplementedError("Method not implemented")
