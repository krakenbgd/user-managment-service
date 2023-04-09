import os

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

db_host = os.getenv("PG_DB_HOST")
db_user = os.getenv("PG_DB_USERNAME")
db_password = os.getenv("PG_DB_PASSWORD")
db_name = os.getenv("PG_DB_NAME")

engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}")

# define metadata for the users table
metadata = MetaData(schema="public")
users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("first_name", String),
    Column("last_name", String),
    Column("address", String),
    Column("country", String),
    Column("age", Integer),
)

metadata.create_all(engine)
