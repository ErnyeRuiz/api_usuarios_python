from typing import Optional
from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.schemas import UserInDB, UserLogin

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def login(self, user: UserLogin) -> Optional[UserInDB]:
        """
        Ejecuta una funcion para hacer login
        """
        query = text(
            "SELECT * FROM login(:username, :password)"
        )
        params = {
            "username": user.username,
            "password": user.password,
            "": None  # Parámetro de salida va a ser null o un usuario (model usuario)
        }

        try:
            result = await self.db.execute(query, params)
            user_data = result.mappings().first()

            if user_data:
                return UserInDB(**user_data)
            return None
        except Exception as e:
            await self.db.rollback()
            raise HTTPException(
                status_code = 400,
                detail = f'Error en el login: {str(e)}'
            )    