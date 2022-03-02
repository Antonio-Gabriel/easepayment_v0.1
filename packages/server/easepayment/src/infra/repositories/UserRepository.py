from ...repositories import IUserRepository

from ...domain.entityprops import UserProps

from ..sqlAlchemy import engine, user


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
