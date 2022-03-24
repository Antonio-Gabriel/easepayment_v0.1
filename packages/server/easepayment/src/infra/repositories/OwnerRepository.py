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

    def get():
        """get all owners"""

        connection = engine.connect()
        query = select(owner)
        result = connection.execute(query).fetchall()

        return result

    def get_by_id(owner_id: str):
        """get owner by id"""

        connection = engine.connect()
        query = select(owner).where(owner.c.id == owner_id)
        result = connection.execute(query).fetchone()

        return result

    def update(owner_props: OwnerProps):
        """update owner into db"""

        connection = engine.connect()
        statement = (
            owner.update()
            .values(
                {
                    owner.c.name: owner_props.name,
                    owner.c.phone: owner_props.phone,
                    owner.c.email: owner_props.email,
                }
            )
            .where(owner.c.id == owner_props.id)
        )

        result = connection.execute(statement)

        return result

    def delete(owner_id: str):
        """delete owner into db"""

        connection = engine.connect()
        statement = owner.delete().where(owner.c.id == owner_id)

        result = connection.execute(statement)

        return result
