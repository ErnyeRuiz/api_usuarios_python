
from fastapi import HTTPException
from ..repositories.user_repository import UserRepository
from ..models.schemas import UserInDB, UserLogin

class UserService:
    def __init__(self, db):
        self.repository = UserRepository(db)
    
    async def login(self, user: UserLogin) -> UserInDB:
        try:
            user_db = await self.repository.login(user) 
            if not user_db:
                raise HTTPException(
                    status_code = 401,
                    detail = "Credenciales inválidas"
                )
            return user_db
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code = 500,
                detail = "Error interno: " + e
            )