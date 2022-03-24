from sqlalchemy.sql import select
from ..sqlAlchemy import engine, course

from ...repositories import ICourseRepository

from ...domain.entityprops import CourseProps


class CourseRepository(ICourseRepository):
    def save(course_props: CourseProps):
        """Save course"""
        connection = engine.connect()
        statement = course.insert()

        result = connection.execute(
            statement,
            {
                "id": course_props.id,
                "name": course_props.name,
                "state": course_props.state,
            },
        )

        return result

    def find_course(name: str):
        """Find course"""

        connection = engine.connect()
        query = select(course).where(course.c.name == name)
        result = connection.execute(query)

        row = result.fetchone()

        result.close()

        return row

    def delete(courseId: str):
        """delete course"""
