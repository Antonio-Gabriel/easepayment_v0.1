from sqlalchemy.sql import text, select
from ..sqlAlchemy import engine, classe_related_course, course, classe

from ...domain.entityprops import ClassRelatedCourseProps
from ...repositories import IClasseRelatedCourseRepository


class ClasseRelatedCourseRepository(IClasseRelatedCourseRepository):
    def save(related_props: ClassRelatedCourseProps):
        """Related class with student"""

        connection = engine.connect()
        result = connection.execute(
            classe_related_course.insert(),
            {
                "id": related_props.id,
                "classe_id": related_props.classId,
                "course_id": related_props.courseId,
                "price": related_props.price,
            },
        )

        return result

    def get_class_with_courses():
        connection = engine.connect()
        query = select(
            [
                classe_related_course.c.id,
                course.c.name,
                classe.c.name,
                classe_related_course.c.price,
            ]
        ).select_from(
            classe_related_course.outerjoin(
                course, classe_related_course.c.course_id == course.c.id
            ).outerjoin(classe, classe_related_course.c.classe_id == classe.c.id)
        )

        result = connection.execute(query).fetchall()

        return result

    def delete(id: str):
        """delete class related course into db"""

        connection = engine.connect()
        stm = text("SET FOREIGN_KEY_CHECKS=0;")

        connection.execute(stm)

        statement = classe_related_course.delete().where(
            classe_related_course.c.id == id
        )

        result = connection.execute(statement)

        return result
