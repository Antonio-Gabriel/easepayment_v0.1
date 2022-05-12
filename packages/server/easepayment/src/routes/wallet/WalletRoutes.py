from fastapi import APIRouter, status, Depends

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from packages.server.easepayment.src.infra.repositories import WalletRepository
from packages.server.easepayment.src.usecases.wallet.Deposit import Deposit
from packages.server.easepayment.src.usecases.wallet.GetWalletByUser import (
    GetWalletByUser,
)

from packages.server.easepayment.src.usecases.wallet.InitializeWallet import (
    InitializeWallet,
)
from packages.server.easepayment.src.usecases.wallet.WithDraw import WithDraw

from .schema.WalletSchema import WalletSchema

wallet_route = APIRouter(prefix="/api", tags=["Wallet"])


@wallet_route.post("/wallet/{id}/initialize")
async def initialize_wallet(id: str):
    """Initialize wallet"""

    running_wallet = InitializeWallet(WalletRepository)
    result = running_wallet.execute(user_id=id)

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


@wallet_route.get("/wallet/{id}/user")
async def user(id: str):
    """Get user"""
    get_user = GetWalletByUser(WalletRepository)
    result = get_user.execute(id)

    return {"user": result.get_value()}


@wallet_route.post("/wallet/{id}/deposit")
async def deposit(id: str, credentials: WalletSchema):
    """Deposit balance in wallet"""

    deposit_in_wallet = Deposit(WalletRepository)
    result = deposit_in_wallet.execute(user_id=id, amount=credentials.amount)

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


@wallet_route.post("/wallet/{id}/withdraw")
async def withdraw(id: str, credentials: WalletSchema):
    """Withdraw balance in wallet"""

    with_draw_in_wallet = WithDraw(WalletRepository)
    result = with_draw_in_wallet.execute(user_id=id, amount=credentials.amount)

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
