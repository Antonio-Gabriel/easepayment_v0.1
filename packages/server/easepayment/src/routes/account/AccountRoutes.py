from fastapi import APIRouter, status, Depends

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from packages.server.easepayment.src.infra.repositories import AccountRepository
from packages.server.easepayment.src.usecases.account.AccountRequestDTO import (
    AccountRequestDTO,
)
from packages.server.easepayment.src.usecases.account.CreateAccount import CreateAccount
from packages.server.easepayment.src.usecases.account.GetAccountById import (
    GetAccountById,
)
from packages.server.easepayment.src.usecases.account.UpdateAccount import UpdateAccount
from packages.server.easepayment.src.usecases.account.UpdateAccountRequestDTO import (
    UpdateAccountRequestDTO,
)

from .schema.AccountSchema import (
    AccountSchemaRequest,
    AccountSchemaResponse,
    AccountSchemaUpdateRequest,
)

account_routes = APIRouter(prefix="/api", tags=["Account"])


@account_routes.post("/create/account", response_model=AccountSchemaResponse)
async def create(credentials: AccountSchemaRequest):
    """Create user account"""

    create_account = CreateAccount(AccountRepository)
    result = create_account.execute(
        AccountRequestDTO(username=credentials.username, password=credentials.password)
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
                    "username": result.get_value().username,
                    "password": result.get_value().password,
                }
            ),
        )


@account_routes.get("/account/{id}", response_model=AccountSchemaResponse)
async def get(id: str):
    """Get account by id"""

    get_account = GetAccountById(AccountRepository)
    result = get_account.execute(id)

    return {
        "id": result.get_value().id,
        "username": result.get_value().username,
        "password": result.get_value().password,
    }


@account_routes.put("/update/{id}/account", response_model=AccountSchemaResponse)
async def update(id: str, credentials: AccountSchemaUpdateRequest):
    """Update user account"""

    update_account = UpdateAccount(AccountRepository)
    result = update_account.execute(
        UpdateAccountRequestDTO(
            username=credentials.username,
            password=credentials.password,
            currentPassword=credentials.currentPassword,
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
                    "username": result.get_value().username,
                    "password": result.get_value().password,
                }
            ),
        )
