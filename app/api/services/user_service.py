
from http import HTTPStatus
from fastapi import HTTPException

from app.api.models.generic.http_response import ApiResponse, error_response
from ..repositories.user_repository import UserRepository
from ..models.schemas import User, UserInDB, UserLogin
from app.api.services.user_security.user_security_service import UserSecurityService
class UserService:
    def __init__(self, db):
        self.repository = UserRepository(db)    
        
    async def insertUser(self, user: User) -> ApiResponse[int]:
        try:
            response = await self.repository.createUser(user) 
            if response.data == 0:
                return error_response(
                    message="No se pudo crear el usuario",
                    status_code=HTTPStatus.BAD_REQUEST
                )
            return response
        except HTTPException as he:
            raise he
        except Exception as e:
            return error_response(
                message="Error interno del servidor",
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                error_details=str(e)
            )
    
    @classmethod
    def __desencriptar(value: str) -> str:
        return UserSecurityService.desencriptar(value)
