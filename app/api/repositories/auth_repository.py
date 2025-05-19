import re
from typing import Optional, Union
from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.models.generic.http_response import ApiResponse, error_response, success_response
from ..models.schemas import User, UserInDB, UserLogin


class AuthRepository:
    def __init__(self, db: AsyncSession):
        self.db = db     
        
    async def login(self, user: UserLogin) -> ApiResponse[User]:
        try:
            query = text(
                "CALL sp_login(:p_nombre_usuario, :p_contrasena)"
                )
            result = await self.db.execute(query, {
                "p_nombre_usuario": user.username,                 
                "p_contrasena": user.password
            })

            row = result.fetchone()
            if not row:
                return error_response("Error en el procedimiento almacenado")
        
            if len(row) == 1:  # Si solo retorna un campo (código)
                if row[0] == 0:
                    return error_response("Credenciales inválidas", status_code=401)
                return error_response("Error desconocido", status_code=400)
            
            # Si tiene múltiples campos, asumimos que es el usuario
            user_data = {
                'usuarioID': row[0],
                'nombre': row[1],
                'apellidos': row[2],
                'cedula': row[3],
                'fechaNacimiento': row[4],
                'fechaRegistro': row[5],
                'nombreUsuario': row[6],
            }            

            return success_response(data = User(**user_data), message="Login exitoso")     
     
        except Exception as e:
            await self.db.rollback()
            raise HTTPException(
                status_code=400,
                detail=error_response(
                    message="Error en base de datos",
                    error_details=e
                ).model_dump()
            )
    
def extraer_error_personalizado(error: Exception) -> str:
    mensaje = str(error)
    # Busca el mensaje entre los delimitadores #
    coincidencia = re.search(r"#(.*?)#", mensaje)
    if coincidencia:
        return coincidencia.group(1).strip()
    return "Error interno del servidor"