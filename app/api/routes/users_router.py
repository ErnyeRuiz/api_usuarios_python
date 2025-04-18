from fastapi import APIRouter, Depends, HTTPException, status

from app.api.core.database import get_db
from app.api.services.user_service import UserService
from ..models.schemas import UserInDB, UserLogin
from sqlalchemy.ext.asyncio import AsyncSession

user_router = APIRouter(prefix="/users", tags=["users"])

@user_router.api_route(
    "/login",
    methods = ["POST", "OPTIONS"],
    response_model = UserInDB,
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
        return user
    except HTTPException:
        raise
    except Exception:
        raise
