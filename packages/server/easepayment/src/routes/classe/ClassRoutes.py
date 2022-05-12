from fastapi import APIRouter, status, Depends

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from packages.server.easepayment.src.infra.repositories import (
    ClasseRelatedCourseRepository,
)
from packages.server.easepayment.src.usecases.classCourse.ClassRelatedCourse import (
    ClassRelatedCourse,
)
from packages.server.easepayment.src.usecases.classCourse.ClassRelatedCourseRequestDTO import (
    ClassRelatedCourseRequestDTO,
)
from packages.server.easepayment.src.usecases.classCourse.DeleteClassRelatedCourse import (
    DeleteClassRelatedCourse,
)
from packages.server.easepayment.src.usecases.classCourse.GetClassWithCourse import (
    GetClassWithCourse,
)

from .schema.ClassSchema import ClassSchema, ClassSchemaRequest, ClassSchemaList

class_routes = APIRouter(prefix="/api", tags=["Classe"])


@class_routes.post("/class/course", response_model=ClassSchema)
async def create(credentials: ClassSchemaRequest):
    """Add course into class"""

    create_class_related_course = ClassRelatedCourse(ClasseRelatedCourseRepository)
    result = create_class_related_course.execute(
        ClassRelatedCourseRequestDTO(
            classId=credentials.classe_id,
            courseId=credentials.course_id,
            price=credentials.price,
        )
    )

    error = result.error_value()

    if error:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder(
                {
                    "detail": error,
                }
            ),
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "id": result.get_value().id,
                    "classe_id": result.get_value().classId,
                    "course_id": result.get_value().courseId,
                    "price": result.get_value().price,
                }
            ),
        )


@class_routes.delete("/class/course/{id}/delete", response_model=ClassSchema)
async def delete(id: str):
    """delete course into class"""

    delete_class_related_course = DeleteClassRelatedCourse(
        ClasseRelatedCourseRepository
    )
    result = delete_class_related_course.execute(id=id)

    error = result.error_value()

    if error:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder(
                {
                    "detail": error,
                }
            ),
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "id": result.get_value().id,
                    "classe_id": result.get_value().classId,
                    "course_id": result.get_value().courseId,
                    "price": result.get_value().price,
                }
            ),
        )


@class_routes.get("/class/course", response_model=ClassSchemaList)
async def get_class_related_course():
    """Get courses with the classes"""

    get_class_with_courses = GetClassWithCourse(ClasseRelatedCourseRepository)
    result = get_class_with_courses.execute()

    return {"courses": result.get_value()}
