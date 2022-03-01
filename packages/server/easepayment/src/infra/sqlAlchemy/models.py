from datetime import datetime

from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    MetaData,
    ForeignKey,
    Boolean,
    DateTime,
)

engine = create_engine("mysql+pymysql://root:root@localhost/exercicio")
metadata_object = MetaData(bind=engine)

owner = Table(
    "owner",
    metadata_object,
    Column("id", String(40), nullable=False, primary_key=True),
    Column("name", String(60), nullable=False),
    Column("phone", String(14), nullable=False),
    Column("email", String(60), nullable=False),
)

account = Table(
    "account",
    metadata_object,
    Column("id", String(40), nullable=False, primary_key=True),
    Column("username", String(40), nullable=False),
    Column("password", String(80), nullable=False),
)

user = Table(
    "user",
    metadata_object,
    Column("id", String(40), nullable=False, primary_key=True),
    Column("account_id", String(40), ForeignKey("account.id")),
    Column("owner_id", String(40), ForeignKey("owner.id")),
    Column("state", Boolean, default=True),
    Column("created_at", DateTime, default=datetime.now),
    Column("updated_at", DateTime, default=datetime.now, onupdate=datetime.now),
)


metadata_object.create_all()
