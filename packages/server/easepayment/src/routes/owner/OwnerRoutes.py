from fastapi import APIRouter, status, Depends

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from packages.server.easepayment.src.infra.repositories import (
    OwnerRelatedStudentRepository,
    OwnerRepository,
)
from packages.server.easepayment.src.usecases.owner.CreateOwner import CreateOwner
from packages.server.easepayment.src.usecases.owner.DeleteOwner import DeleteOwner
from packages.server.easepayment.src.usecases.owner.GetOwnderById import GetOwnderById
from packages.server.easepayment.src.usecases.owner.GetOwners import GetOwners
from packages.server.easepayment.src.usecases.owner.OwnerRequestDTO import (
    OwnerRequestDTO,
)
from packages.server.easepayment.src.usecases.owner.UpdateOwner import UpdateOwner
from packages.server.easepayment.src.usecases.ownerStudent.GetStudentsRelatedOwner import (
    GetStudentsRelatedOwner,
)
from packages.server.easepayment.src.usecases.ownerStudent.RelatedStudentInOwner import (
    RelatedStudentInOwner,
)
from packages.server.easepayment.src.usecases.ownerStudent.RelatedStudentInOwnerRequestDTO import (
    RelatedStudentInOwnerRequestDTO,
)
from packages.server.easepayment.src.usecases.ownerStudent.UnrelatedStudentInOwner import (
    UnrelatedStudentInOwner,
)

from .schema.OwnerSchema import (
    OwnerSchemaRequest,
    OwnerSchema,
    OwnerSchemaList,
    OwnerRelatedStudentSchemaRequest,
    OwnerRelatedStudentSchema,
)

owner_route = APIRouter(prefix="/api", tags=["Owner"])


@owner_route.post("/create-owner", response_model=OwnerSchema)
async def create(credentials: OwnerSchemaRequest):
    """Create owner"""
    create_owner = CreateOwner(OwnerRepository)
    result = create_owner.execute(
        OwnerRequestDTO(
            name=credentials.name,
            email=credentials.email,
            phone=credentials.phone,
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
                }
            ),
        )


@owner_route.get("/owners", response_model=OwnerSchemaList)
async def get():
    """Get all owners"""
    get_all_owners = GetOwners(OwnerRepository)
    result = get_all_owners.execute()

    return {"owners": result.get_value()}


@owner_route.get("/owner/{id}/students", response_model=OwnerRelatedStudentSchema)
async def get_students_related_owner(id: str):
    """Get students related owner"""
    get_student_related_courses = GetStudentsRelatedOwner(OwnerRelatedStudentRepository)
    result = get_student_related_courses.execute(id)

    return {"students": result.get_value()}


@owner_route.get("/owner/{id}", response_model=OwnerSchema)
async def get_owner_by_id(id: str):
    """Get all owners"""
    get_all_owners = GetOwnderById(OwnerRepository)
    result = get_all_owners.execute(id)

    return {
        "id": result.get_value().id,
        "name": result.get_value().name,
        "email": result.get_value().email,
        "phone": result.get_value().phone,
    }


@owner_route.put("/owner/{id}/update", response_model=OwnerSchema)
async def update(id: str, credentials: OwnerSchemaRequest):
    """Update owner"""
    update_owner = UpdateOwner(OwnerRepository)
    result = update_owner.execute(
        OwnerRequestDTO(
            name=credentials.name,
            email=credentials.email,
            phone=credentials.phone,
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
                }
            ),
        )


@owner_route.delete("/owner/{id}/delete")
async def delete(id: str):
    """Delete owner"""
    delete_owner = DeleteOwner(OwnerRepository)
    result = delete_owner.execute(id)

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


@owner_route.post("/related-student-to-owner")
async def owner_related_student(credentials: OwnerRelatedStudentSchemaRequest):
    """Related student to owner"""
    related_student = RelatedStudentInOwner(OwnerRelatedStudentRepository)
    result = related_student.execute(
        RelatedStudentInOwnerRequestDTO(
            studentId=credentials.studentId,
            ownerId=credentials.ownerId,
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
                    "msg": "Associeted",
                }
            ),
        )


@owner_route.delete("/unrelated-student-to-owner")
async def owner_unrelated_student(credentials: OwnerRelatedStudentSchemaRequest):
    """Related student to owner"""
    related_student = UnrelatedStudentInOwner(OwnerRelatedStudentRepository)
    result = related_student.execute(
        student_id=credentials.studentId,
        owner_id=credentials.ownerId,
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
                    "msg": "Unrelated",
                }
            ),
        )
