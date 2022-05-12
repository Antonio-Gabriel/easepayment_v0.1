from fastapi import APIRouter, status, Depends

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from packages.server.easepayment.src.infra.repositories import (
    StudentAutoRelatedRepository,
    StudentRepository,
)
from packages.server.easepayment.src.usecases.student.AutoRelatedStudent import (
    AutoRelatedStudent,
)
from packages.server.easepayment.src.usecases.student.AutoRelatedStudentDTO import (
    AutoRelatedStudentDTO,
)
from packages.server.easepayment.src.usecases.student.CreateStudent import CreateStudent
from packages.server.easepayment.src.usecases.student.DeleteStudent import DeleteStudent
from packages.server.easepayment.src.usecases.student.GetStudentById import (
    GetStudentById,
)
from packages.server.easepayment.src.usecases.student.GetStudents import GetStudents
from packages.server.easepayment.src.usecases.student.StudentRequestDTO import (
    StudentRequestDTO,
)
from packages.server.easepayment.src.usecases.student.UnrelatedStudent import (
    UnrelatedStudent,
)
from packages.server.easepayment.src.usecases.student.UpdateStudent import UpdateStudent

from .schema.StudentSchema import (
    StudentSchemaRequest,
    StudentSchema,
    StudentSchemaList,
    StudentAutoRelatedSchema,
    StudentAutoRelatedSchemaResponse,
)

student_route = APIRouter(prefix="/api", tags=["Student"])


@student_route.post("/create-student", response_model=StudentSchema)
async def create(credentials: StudentSchemaRequest):
    """Create student"""
    create_student = CreateStudent(StudentRepository)
    result = create_student.execute(
        StudentRequestDTO(
            name=credentials.name,
            email=credentials.email,
            phone=credentials.phone,
            process=credentials.process,
            avatar="",
            district=credentials.district,
            location=credentials.location,
            studentId="",
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
                    "name": result.get_value().name,
                    "email": result.get_value().email,
                    "phone": result.get_value().phone,
                    "process": result.get_value().process,
                    "district": result.get_value().district,
                    "location": result.get_value().location,
                }
            ),
        )


@student_route.get("/students", response_model=StudentSchemaList)
async def get():
    """Get all students"""
    get_all_students = GetStudents(StudentRepository)
    result = get_all_students.execute()

    return {"students": result.get_value()}


@student_route.get("/student/{id}", response_model=StudentSchema)
async def get_student_by_id(id: str):
    """Get student by id"""
    get_user_by_id = GetStudentById(StudentRepository)
    result = get_user_by_id.execute(id)

    return {
        "id": result.get_value().id,
        "name": result.get_value().name,
        "email": result.get_value().email,
        "phone": result.get_value().phone,
        "process": result.get_value().process,
        "district": result.get_value().district,
        "location": result.get_value().location,
    }


@student_route.put("/student/{id}/update", response_model=StudentSchema)
async def update(id: str, credentials: StudentSchemaRequest):
    """Update student"""
    update_student = UpdateStudent(StudentRepository)
    result = update_student.execute(
        StudentRequestDTO(
            name=credentials.name,
            email=credentials.email,
            phone=credentials.phone,
            process=credentials.process,
            avatar="",
            district=credentials.district,
            location=credentials.location,
            studentId="",
        ),
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
                    "email": result.get_value().email,
                    "phone": result.get_value().phone,
                    "process": result.get_value().process,
                    "district": result.get_value().district,
                    "location": result.get_value().location,
                }
            ),
        )


@student_route.delete("/student/{process}/delete")
async def delete(process: int):
    """Delete student"""
    delete_student = DeleteStudent(StudentRepository)
    result = delete_student.execute(process=process)

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


@student_route.post("/related-student", response_model=StudentAutoRelatedSchemaResponse)
async def auto_related(credentials: StudentAutoRelatedSchema):
    """Auto related student"""
    auto_related = AutoRelatedStudent(StudentAutoRelatedRepository)
    result = auto_related.execute(
        AutoRelatedStudentDTO(
            owner_studentId=credentials.owner_studentId,
            studentId=credentials.studentId,
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
                    "student_id": result.get_value().student_id,
                    "owner_studentId": result.get_value().owner_studentId,
                }
            ),
        )


@student_route.delete(
    "/unrelated-student", response_model=StudentAutoRelatedSchemaResponse
)
async def auto_related(credentials: StudentAutoRelatedSchema):
    """Unrelated student"""
    unrelated = UnrelatedStudent(StudentAutoRelatedRepository)
    result = unrelated.execute(
        AutoRelatedStudentDTO(
            owner_studentId=credentials.owner_studentId,
            studentId=credentials.studentId,
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
                    "msg": result.get_value(),
                }
            ),
        )
