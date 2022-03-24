from sqlalchemy.sql import select
from ..sqlAlchemy import engine, account

from ...repositories import IAccountRepository

from ...domain.entityprops import AccountProps


class AccountRepository(IAccountRepository):
    def save(account_props: AccountProps):
        """Save account into db"""

        connection = engine.connect()
        statement = account.insert()

        result = connection.execute(
            statement,
            {
                "id": account_props.id,
                "username": account_props.username,
                "password": account_props.password,
            },
        )

        return result

    def find_by_id(account_id: str):
        """Find account by id"""

        connection = engine.connect()
        query = select(account).where(account.c.id == account_id)
        result = connection.execute(query)

        row = result.fetchone()

        result.close()

        return row

    def update(account_props: AccountProps, id):
        """update account"""

        connection = engine.connect()
        statement = (
            account.update()
            .values(
                {
                    account.c.username: account_props.username,
                    account.c.password: account_props.password,
                }
            )
            .where(account.c.id == id)
        )

        result = connection.execute(statement)

        return result
