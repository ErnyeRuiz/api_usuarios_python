
from http import HTTPStatus
from fastapi import HTTPException

from app.api.models.generic.http_response import ApiResponse, error_response
from app.api.repositories.auth_repository import AuthRepository
from ..models.schemas import User, UserLogin
from app.api.services.user_security.user_security_service import UserSecurityService

class AuthService:
    def __init__(self, db):
        self.repository = AuthRepository(db)    
        
    async def login(self, user: UserLogin) -> ApiResponse[User]:
        try:
            return await self.repository.login(user)
            
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
