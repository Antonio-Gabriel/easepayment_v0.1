from ...repositories import IAccountRepository

from ...domain.entityprops import AccountProps

from ..sqlAlchemy import engine, account


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
