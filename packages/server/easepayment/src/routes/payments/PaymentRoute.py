from fastapi import APIRouter, status, Depends

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from packages.server.easepayment.src.infra.repositories import MonthlyRepository
from packages.server.easepayment.src.infra.repositories.UniformRepository import (
    UniformRepository,
)
from packages.server.easepayment.src.usecases.monthly.GetMonthlyPayed import (
    GetMonthlyPayed,
)
from packages.server.easepayment.src.usecases.monthly.MonthlyPayment import (
    MonthlyPayment,
)
from packages.server.easepayment.src.usecases.monthly.MonthlyRequestDTO import (
    MonthlyRequestDTO,
)
from packages.server.easepayment.src.usecases.uniform.CreateUniformType import (
    CreateUniformType,
)
from packages.server.easepayment.src.usecases.uniform.GetPayedUniformType import (
    GetPayedUniformType,
)
from packages.server.easepayment.src.usecases.uniform.GetUniformType import (
    GetUniformType,
)
from packages.server.easepayment.src.usecases.uniform.UniformPayment import (
    UniformPayment,
)
from packages.server.easepayment.src.usecases.uniform.UniformPaymentRequestDTO import (
    UniformPaymentRequestDTO,
)
from packages.server.easepayment.src.usecases.uniform.UniformTypeRequestDTO import (
    UniformTypeRequestDTO,
)

from .schema.PaymentSchema import PaymentSchema, UniformTypeSchema, UniformPaymentSchema

payment_route = APIRouter(prefix="/api", tags=["Payments"])


@payment_route.post("/pay-month")
async def pay_month(credentials: PaymentSchema):
    """Pay Monthly"""

    month_payed = MonthlyPayment(MonthlyRepository)
    result = month_payed.execute(
        MonthlyRequestDTO(
            userId=credentials.userId,
            studentId=credentials.studentId,
            month=credentials.month,
            value=credentials.value,
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
            content=jsonable_encoder({"msg": result.get_value()}),
        )


@payment_route.get("/monthly-payed/{id}")
async def monthly_payed(id: str):

    get_monthly_payed = GetMonthlyPayed(MonthlyRepository)
    result = get_monthly_payed.execute(id)

    return {"months": result.get_value()}


@payment_route.post("/uniform-type")
async def uniform_type(credentials: UniformTypeSchema):

    save_uniform_type = CreateUniformType(UniformRepository)
    result = save_uniform_type.execute(
        UniformTypeRequestDTO(type=credentials.type, price=credentials.price)
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


@payment_route.get("/uniform-types")
async def uniform_types():

    get_uniform_types = GetUniformType(UniformRepository)
    result = get_uniform_types.execute()

    return {"uniforms": result.get_value()}


@payment_route.post("/pay-uniform")
async def pay_uniform(credentials: UniformPaymentSchema):

    pay_uniform = UniformPayment(UniformRepository)
    result = pay_uniform.execute(
        UniformPaymentRequestDTO(
            userId=credentials.userId,
            studentId=credentials.studentId,
            uniform_type_type=credentials.uniform_type_type,
            amount=credentials.amount,
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
            content=jsonable_encoder({"msg": result.get_value()}),
        )


@payment_route.get("/uniforms-payed/{id}")
async def uniforms(id: str):

    get_uniforms_payed = GetPayedUniformType(UniformRepository)
    result = get_uniforms_payed.execute(id)

    return {"uniforms": result.get_value()}
