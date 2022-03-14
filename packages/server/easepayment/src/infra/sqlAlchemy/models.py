#!python3
from datetime import datetime

from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    Float,
    String,
    Text,
    MetaData,
    ForeignKey,
    Boolean,
    DateTime,
    TIMESTAMP,
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

student = Table(
    "student",
    metadata_object,
    Column("id", String(40), nullable=False, primary_key=True),
    Column("process", Integer, nullable=False),
    Column("name", String(60), nullable=False),
    Column("phone", String(14), nullable=False),
    Column("email", String(60), nullable=False),
    Column("district", String(45), nullable=False),
    Column("location", String(45), nullable=False),
    Column("avatar", Text, nullable=False),
    Column("state", Boolean, default=True),
    Column("student_id", String(40), ForeignKey("student.id")),
)

classe = Table(
    "classe",
    metadata_object,
    Column("id", String(40), nullable=False, primary_key=True),
    Column("name", String(60), nullable=False),
    Column("state", Boolean, default=True),
    Column("created_at", TIMESTAMP, default=datetime.now),
    Column("updated_at", TIMESTAMP, default=datetime.now, onupdate=datetime.now),
)

course = Table(
    "course",
    metadata_object,
    Column("id", String(40), nullable=False, primary_key=True),
    Column("name", String(60), nullable=False),
    Column("state", Boolean, default=True),
    Column("created_at", TIMESTAMP, default=datetime.now),
    Column("updated_at", TIMESTAMP, default=datetime.now, onupdate=datetime.now),
)

classe_related_course = Table(
    "class_related_course",
    metadata_object,
    Column("classe_id", String(40), ForeignKey("classe.id")),
    Column("course_id", String(40), ForeignKey("course.id")),
    Column("student_id", String(40), ForeignKey("student.id")),
    Column("price", Float, default=0.00),
)


user = Table(
    "user",
    metadata_object,
    Column("id", String(40), nullable=False, primary_key=True),
    Column("account_id", String(40), ForeignKey("account.id")),
    Column("owner_id", String(40), ForeignKey("owner.id")),
    Column("student_id", String(40), ForeignKey("student.id")),
    Column("state", Boolean, default=True),
    Column("created_at", TIMESTAMP, default=datetime.now),
    Column("updated_at", TIMESTAMP, default=datetime.now, onupdate=datetime.now),
)

owner_related_student = Table(
    "student_related_owner",
    metadata_object,
    Column("owner_id", String(40), ForeignKey("owner.id")),
    Column("student_id", String(40), ForeignKey("student.id")),
)

metadata_object.create_all()
