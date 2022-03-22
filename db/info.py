import sqlalchemy
import datetime

from .base import metadata

#create table with info about user
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key = True, autoincrement = True, unique =  True),
    sqlalchemy.Column("email", sqlalchemy.String, unique =  True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("surname", sqlalchemy.String),
    sqlalchemy.Column("gender", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("hashed_password", sqlalchemy.String)
#   sqlalchemy.Column("photo", sqlalchemy.String)
)
