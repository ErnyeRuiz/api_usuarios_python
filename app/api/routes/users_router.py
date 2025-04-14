from typing import Any, Dict
from fastapi import APIRouter, Depends, HTTPException, status

from app.api.core.database import get_db
from app.api.core.utilities.auth_utils import create_access_token
from app.api.services.user_service import UserService
from ..models.schemas import UserInDB, UserLogin
from sqlalchemy.ext.asyncio import AsyncSession
from ..core.config import settings
user_router = APIRouter(prefix="/users", tags=["users"])

@user_router.api_route(
    "/login",
    methods = ["POST", "OPTIONS"],
    response_model = Dict[str, Any],
    summary = "Iniciar sesión",
    responses = {
        401: {"description": "Credenciales inválidas"},
        500: {"description": "Error interno del servidor"},
    }
)
async def login(
    credentials: UserLogin,
    db: AsyncSession = Depends(get_db)
):    
    """
    Autentica a un usuario usando la función PostgreSQL `login()`.
    
    - **username**: Nombre de usuario, cédula o correo.
    - **password**: Contraseña.
    """     
    try:
        service = UserService(db)
        user = await service.login(credentials)

        access_token = create_access_token(
            data={"sub": user.nombreusuario, "id": str(user.usuarioid)}
        )
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            "user": user.dict()
        }
    except HTTPException:
        raise
    except Exception:
        raise
