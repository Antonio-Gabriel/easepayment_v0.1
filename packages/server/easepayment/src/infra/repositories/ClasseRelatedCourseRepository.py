from ..sqlAlchemy import engine, classe_related_course

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

    def delete(related_props: ClassRelatedCourseProps):
        """delete stutend related owner into db"""
