from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from src.schema.user_schema import UserSchema
from src.config.db import engine
from src.model.users import users

user = APIRouter()

@user.get("/user")
def root():
    return {"message": "API User Endpoint is Working"}

@user.get("/api/users")
def get_all_users():
    try:
        # Manejo de conexión con `with`
        with engine.connect() as conn:
            # Ejecutar la consulta para obtener todos los usuarios.
            result = conn.execute(users.select()).mappings().all()

            print("❌❌❌", result)

            # Convertir el resultado a una lista de diccionarios
            users_list = [dict(row) for row in result]

            return users_list
    except SQLAlchemyError as e:
        # Manejo de errores de la base de datos
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@user.post("/api/createUser")
def create_user(data_user: UserSchema):
    try:
        # Convertir el modelo recibido en un diccionario
        new_user = data_user.model_dump()

        # Verificar si la imagen está presente y es una cadena válida
        if not new_user.get("perfilImage"):
            raise HTTPException(status_code=400, detail="Image is required in Base64 format")

        # Guardar el usuario en la base de datos
        with engine.connect() as conn:
            conn.execute(users.insert().values(new_user))
            conn.commit()

        return {
            "message": "Successfully created",
            "user": new_user
        }
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
