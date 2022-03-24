from sqlalchemy.sql import select, text
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

    def update(course_props: CourseProps):
        """update course"""

        connection = engine.connect()
        statement = (
            course.update()
            .values({course.c.name: course_props.name})
            .where(course.c.id == course_props.id)
        )

        result = connection.execute(statement)

        return result

    def get():
        """get all course"""

        connection = engine.connect()
        query = select(course)
        result = connection.execute(query).fetchall()

        return result

    def get_by_id(course_id: str):
        """get course by id"""

        connection = engine.connect()
        query = select(course).where(course.c.id == course_id)
        result = connection.execute(query).fetchone()

        return result

    def delete(courseId: str):
        """delete course"""

        connection = engine.connect()
        statement = (
            course.update()
            .values(
                {
                    course.c.state: False,
                }
            )
            .where(course.c.id == courseId)
        )

        result = connection.execute(statement)

        return result
