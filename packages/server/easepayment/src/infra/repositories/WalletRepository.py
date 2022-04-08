from sqlalchemy.sql import select
from ..sqlAlchemy import engine, wallet

from ...repositories import IWalletRepository


class WalletRepository(IWalletRepository):
    def deposit(amount: float, user_id: str):
        """Deposit balance in account"""

        connection = engine.connect()
        statement = (
            wallet.update()
            .values({wallet.c.balance: amount})
            .where(wallet.c.user_id == user_id)
        )

        result = connection.execute(statement)

        return result

    def with_draw(amount: float, user_id: str):
        """WithDraw balance in account"""

        connection = engine.connect()
        statement = (
            wallet.update()
            .values({wallet.c.balance: amount})
            .where(wallet.c.user_id == user_id)
        )

        result = connection.execute(statement)

        return result

    def initialize(user_id: str):
        """Initialize wallet"""

        connection = engine.connect()
        statement = wallet.insert()

        result = connection.execute(
            statement,
            {"id": user_id.id, "balance": user_id.balance, "user_id": user_id.userId},
        )

        return result

    def get_by_id(user_id: str):
        """Get state of wallet"""

        connection = engine.connect()
        query = select(wallet).where(wallet.c.user_id == user_id)
        result = connection.execute(query)

        row = result.fetchone()

        result.close()

        return row
