import re
from typing import Optional
from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.models.generic.http_response import ApiResponse, error_response, success_response
from ..models.schemas import User, UserInDB, UserLogin

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
        
    async def createUser(self, user: User) -> ApiResponse[int]:
        try:
            query = text(
                "CALL InsertUser(:_nombre, :_apellidos, :_cedula, :_fechaNacimiento, :_nombreUsuario, :_contrasena)"
                )
            result = await self.db.execute(query, {
                "_nombre": user.nombre, 
                "_apellidos": user.apellidos, 
                "_cedula": user.cedula, 
                "_fechaNacimiento": user.fechaNacimiento, 
                "_nombreUsuario": user.nombreUsuario, 
                "_contrasena": user.contrasena
            })

            usuario_id = result.scalar_one()
            await self.db.commit()
            return success_response(data=usuario_id, message="Usuario creado")
        
        except Exception as e:
            await self.db.rollback()
            raise HTTPException(
                status_code=400,
                detail=error_response(
                    message="Error en base de datos",
                    error_details=extraer_error_personalizado(e)
                ).model_dump()
            )
    
def extraer_error_personalizado(error: Exception) -> str:
    mensaje = str(error)
    # Busca el mensaje entre los delimitadores #
    coincidencia = re.search(r"#(.*?)#", mensaje)
    if coincidencia:
        return coincidencia.group(1).strip()
    return "Error interno del servidor"