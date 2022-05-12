from sqlalchemy.sql import select
from ..sqlAlchemy import engine, user, account, owner

from ...repositories import IUserRepository

from ...domain.entityprops import UserProps


class UserRepository(IUserRepository):
    def save(user_props: UserProps):
        """Save account into db"""

        connection = engine.connect()
        statement = user.insert()

        result = connection.execute(
            statement,
            {
                "id": user_props.id,
                "account_id": user_props.account_id,
                "owner_id": user_props.owner_id,
                "student_id": user_props.student_id,
                "state": user_props.state,
            },
        )

        return result

    def get(user_id: str):
        """Get user by id"""
        connection = engine.connect()
        query = (
            select(
                [
                    user.c.id,
                    owner.c.id,
                    owner.c.name,
                    account.c.username,
                    owner.c.email,
                    owner.c.phone,
                    user.c.created_at,
                    user.c.updated_at,
                ]
            )
            .select_from(
                user.outerjoin(account, user.c.account_id == account.c.id).outerjoin(
                    owner, user.c.owner_id == owner.c.id
                )
            )
            .where(user.c.id == user_id)
        )

        result = connection.execute(query).fetchone()

        return result

    def get_user_by_owner_id(owner_id: str):
        """Get user by owner id"""
        connection = engine.connect()
        query = (
            select(
                [
                    user.c.id,
                    account.c.password,
                ]
            )
            .select_from(
                user.outerjoin(account, user.c.account_id == account.c.id).outerjoin(
                    owner, user.c.owner_id == owner.c.id
                )
            )
            .where(user.c.owner_id == owner_id)
        )

        result = connection.execute(query).fetchone()

        return result

    def remove(user_id: str):
        """Remove user into db"""

        connection = engine.connect()
        statement = (
            user.update()
            .values(
                {
                    user.c.id: user_id,
                }
            )
            .where(user.c.state == 0)
        )

        result = connection.execute(statement)

        return result
