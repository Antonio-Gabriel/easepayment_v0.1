from fastapi import APIRouter, status, Depends

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from packages.server.easepayment.src.config.AuthMiddleware import AuthMiddleware
from packages.server.easepayment.src.infra.repositories import (
    UserRepository,
    OwnerRepository,
)

from packages.server.easepayment.src.usecases.user.CreateUser import CreateUser
from packages.server.easepayment.src.usecases.user.DeleteUser import DeleteUser
from packages.server.easepayment.src.usecases.user.GetUserById import GetUserById
from packages.server.easepayment.src.usecases.user.SignInUser import SignInUser
from packages.server.easepayment.src.usecases.user.UserRequestDTO import UserRequestDTO

from .schema.UserSchema import (
    UserSchemaRequest,
    UserSchemaResponse,
)

from .schema.UserAuthSchema import UserAuthSchema

user_route = APIRouter(prefix="/api", tags=["User"])


@user_route.post("/auth")
async def auth(credentials: UserAuthSchema):
    """Sign in user"""
    user_account = SignInUser(OwnerRepository)
    result = user_account.execute(credentials.email, credentials.password)

    error = result.error_value()

    if error:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content=jsonable_encoder(
                {
                    "detail": error,
                }
            ),
        )
    else:
        return {
            "access_token": AuthMiddleware.encode_token(result.get_value()[0]),
            "token_type": "Bearer",
            "user": result.get_value(),
        }


@user_route.post("/create/user", response_model=UserSchemaResponse)
async def create(credentials: UserSchemaRequest):
    """Create user account"""

    create_user = CreateUser(UserRepository)
    result = create_user.execute(
        UserRequestDTO(
            account_id=credentials.account_id,
            owner_id=credentials.owner_id,
            student_id=credentials.student_id,
            state=True,
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
                    "account_id": result.get_value().account_id,
                    "owner_id": result.get_value().owner_id,
                    "state": result.get_value().state,
                    "created_at": result.get_value().created_at,
                    "updated_at": result.get_value().updated_at,
                }
            ),
        )


@user_route.get("/user/{id}")
async def get_user_by_id(id: str):
    """Get user by id"""

    get_user = GetUserById(UserRepository)
    result = get_user.execute(id)

    return {"user": result.get_value()}


@user_route.delete("/create/{id}/delete")
async def delete(id: str):
    """Delete user account"""

    delete_user = DeleteUser(UserRepository)
    result = delete_user.execute(id)

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
