import uvicorn

# import unittest
# from packages.server.easepayment import ResolvingSeeder

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from packages.server.easepayment.src.routes.owner.OwnerRoutes import owner_route
from packages.server.easepayment.src.routes.classe.ClassRoutes import class_routes
from packages.server.easepayment.src.routes.courses.CourseRoutes import course_route
from packages.server.easepayment.src.routes.student.StudentRoute import student_route
from packages.server.easepayment.src.routes.enrollment.EnrollmentRoute import (
    enrollment_route,
)

from packages.server.easepayment.src.routes.user.UserRoutes import user_route
from packages.server.easepayment.src.routes.wallet.WalletRoutes import wallet_route
from packages.server.easepayment.src.routes.payments.PaymentRoute import payment_route
from packages.server.easepayment.src.routes.account.AccountRoutes import account_routes

app = FastAPI(redoc_url=False)

app.title = "EasePayment"
app.description = "Documentation easepayment"


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["About"])
def say_hello():
    """Greeting"""
    return {"msg": "Easepayment documentation"}


app.include_router(course_route)
app.include_router(class_routes)
app.include_router(owner_route)
app.include_router(student_route)
app.include_router(enrollment_route)
app.include_router(account_routes)
app.include_router(user_route)
app.include_router(wallet_route)
app.include_router(payment_route)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

    # seeder = ResolvingSeeder()
    # seeder.load_entities_from_json_file(name="Classe")
    # unittest.main()
