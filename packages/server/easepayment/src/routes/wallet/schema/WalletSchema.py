from pydantic import BaseModel


class WalletSchema(BaseModel):
    amount: float
