from databases import Database
from sqlalchemy import create_engine, MetaData

from core.config import DATABASE_URL

#connect db
database = Database(DATABASE_URL)
metadata = MetaData()

#only for sync requst
engine = create_engine(
    DATABASE_URL,
)
