from fastapi import APIRouter, status, Depends

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from packages.server.easepayment.src.infra.repositories import EnrollmentRepository
from packages.server.easepayment.src.usecases.enrollment.CreateEnrollment import (
    CreateEnrollment,
)
from packages.server.easepayment.src.usecases.enrollment.DeleteEnrollment import (
    DeleteEnrollment,
)
from packages.server.easepayment.src.usecases.enrollment.EnrollmentRequestDTO import (
    EnrollmentRequestDTO,
)

from .schema.EnrollmentSchema import (
    EnrollmentSchemaRequest,
    EnrollmentSchema,
)

enrollment_route = APIRouter(prefix="/api", tags=["Enrollment"])


@enrollment_route.post("/enrollment", response_model=EnrollmentSchema)
async def enrollment(credentials: EnrollmentSchemaRequest):
    """Enrollment student"""
    create_enrollment = CreateEnrollment(EnrollmentRepository)
    result = create_enrollment.execute(
        EnrollmentRequestDTO(
            class_related_course_id=credentials.class_related_course_id,
            student_id=credentials.student_id,
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
                    "class_related_course_id": result.get_value().class_related_course_id,
                    "student_id": result.get_value().student_id,
                    "created_at": result.get_value().created_at,
                    "updated_at": result.get_value().updated_at,
                }
            ),
        )


@enrollment_route.delete("/enrollment/delete")
async def enrollment(credentials: EnrollmentSchemaRequest):
    """Remove enrollment student"""
    create_enrollment = DeleteEnrollment(EnrollmentRepository)
    result = create_enrollment.execute(
        class_related_course_id=credentials.class_related_course_id,
        student_id=credentials.student_id,
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
            content=jsonable_encoder({"msg": result.get_value()}),
        )
