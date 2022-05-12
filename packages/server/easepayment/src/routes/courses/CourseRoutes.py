from fastapi import APIRouter, status, Depends

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from packages.server.easepayment.src.infra.repositories import CourseRepository
from packages.server.easepayment.src.usecases.course.GetCourses import GetCourses
from packages.server.easepayment.src.usecases.course.DeleteCourse import DeleteCourse
from packages.server.easepayment.src.usecases.course.CreateCourse import CreateCourse
from packages.server.easepayment.src.usecases.course.CourseRequestDTO import (
    CourseRequestDTO,
)
from packages.server.easepayment.src.usecases.course.UpdateCourse import UpdateCourse
from packages.server.easepayment.src.usecases.course.GetCourseById import GetCourseById

from .schema.CourseSchema import (
    CourseSchema,
    CourseSchemaList,
    CourseSchemaRequest,
    CourseSchemaRequestUpdate,
)

course_route = APIRouter(prefix="/api", tags=["Courses"])


@course_route.post("/create", response_model=CourseSchema)
async def create(credentials: CourseSchemaRequest):
    """Create course"""

    create_course = CreateCourse(CourseRepository)
    result = create_course.execute(CourseRequestDTO(name=credentials.name, state=True))

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
                    "name": result.get_value().name,
                    "state": result.get_value().state,
                    "created_at": result.get_value().created_at,
                    "updated_at": result.get_value().updated_at,
                }
            ),
        )


@course_route.get("/courses", response_model=CourseSchemaList)
async def list_courses():
    """Get all courses"""

    get_all_courses = GetCourses(CourseRepository)
    result = get_all_courses.execute()

    return {"courses": result.get_value()}


@course_route.get("/course/{id}", response_model=CourseSchema)
async def list_courses(id: str):
    """Get course by id"""

    course_by_id = GetCourseById(CourseRepository)
    result = course_by_id.execute(id)

    return {
        "id": result.get_value().id,
        "name": result.get_value().name,
        "state": result.get_value().state,
        "created_at": result.get_value().created_at,
        "updated_at": result.get_value().updated_at,
    }


@course_route.put("/course/{id}/update", response_model=CourseSchema)
async def update(id: str, credentials: CourseSchemaRequestUpdate):
    """Update course"""

    update_course = UpdateCourse(CourseRepository)
    result = update_course.execute(
        CourseRequestDTO(name=credentials.name, state=credentials.state),
        id=id,
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
                    "name": result.get_value().name,
                    "state": result.get_value().state,
                    "created_at": result.get_value().created_at,
                    "updated_at": result.get_value().updated_at,
                }
            ),
        )


@course_route.delete("/course/{id}/delete")
async def delete(id: str):
    """Delete course"""

    delete_course = DeleteCourse(CourseRepository)
    result = delete_course.execute(id)

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
                    "msg": result.get_value(),
                }
            ),
        )
