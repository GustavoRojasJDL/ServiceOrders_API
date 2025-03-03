# database.py

from peewee import SqliteDatabase
from config import DB_NAME

database = SqliteDatabase(
    DB_NAME,
    pragmas={
        "journal_mode": "wal",
        "cache_size": -1 * 64000,  # 64MB
        "foreign_keys": 1,
        "ignore_check_constraints": 0,
        "synchronous": 0,
    },
)


def connect_db():
    """Conecta a la base de datos."""
    database.connect()


def close_db():
    """Cierra la conexión si la base de datos está abierta."""
    if not database.is_closed():
        database.close()
