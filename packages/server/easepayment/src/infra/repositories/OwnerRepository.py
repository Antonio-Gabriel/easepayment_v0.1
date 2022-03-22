from sqlalchemy.sql import select
from ..sqlAlchemy import engine, owner

from ...repositories import IOwnerRepository

from ...domain.entityprops import OwnerProps


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
                "id": owner_props.id,
                "name": owner_props.name,
                "email": owner_props.email,
                "phone": owner_props.phone,
            },
        )

        return result
