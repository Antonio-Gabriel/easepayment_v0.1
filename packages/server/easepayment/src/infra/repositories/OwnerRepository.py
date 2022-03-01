from ...repositories import IOwnerRepository

from ...domain.entityprops import OwnerProps

from sqlalchemy.sql import select
from ..sqlAlchemy import engine, owner


class OwnerRepository(IOwnerRepository):
    def find_by_email(email: str):
        """Find owner by email"""

        connection = engine.connect()
        query = select(owner).where(owner.c.email == email)
        result = connection.execute(query)

        row = result.fetchone()

        result.close()

        return row

    def find_by_phone(phone: str):
        """Find owner by phone number"""

        connection = engine.connect()
        query = select(owner).where(owner.c.phone == phone)
        result = connection.execute(query)

        row = result.fetchone()

        result.close()

        return row

    def save(owner_props: OwnerProps):
        """Save owner into db"""

        connection = engine.connect()
        statement = owner.insert()
        result = connection.execute(
            statement,
            {
                "id": owner_props.get_value().id,
                "name": owner_props.get_value().name,
                "email": owner_props.get_value().email,
                "phone": owner_props.get_value().phone,
            },
        )

        return result
