from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from src.config.db import engine, metadata
from sqlalchemy import Text

# Definir el esquema de la tabla `users`
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, nullable=True),
    Column("name", String(255), nullable=False),
    Column("email", String(255), nullable=False, unique=True),
    Column("password", String(255), nullable=False),
    Column("perfilImage", Text, nullable=False)
)

# Crear las tablas en la base de datos si no existen
try:
    metadata.create_all(engine)
    print("✅ Tablas creadas o verificadas correctamente.")
except Exception as e:
    print(f"❌ Error al crear las tablas: {e}")
