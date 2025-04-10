from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import SQLAlchemyError

# Configuración de la conexión para PostgreSQL
DATABASE_URL = "postgresql://musikMikeDatabase_owner:Q3IfOkr8oxHp@ep-shiny-snowflake-a4kfukhd.us-east-1.aws.neon.tech/musikMikeDatabase?sslmode=require"
engine = create_engine(DATABASE_URL)

# Inicializar MetaData para manejar esquemas de tablas
metadata = MetaData()

# Verificar la conexión
try:
    # Verificar conexión con bloque `with`
    with engine.connect() as conn:
        print("🚀🚀 Conexión exitosa a la base de datos PostgreSQL")
except SQLAlchemyError as e:
    print(f"🚩🚩 Error al conectar con la base de datos: {e}")
