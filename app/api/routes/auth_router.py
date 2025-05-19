from fastapi import APIRouter, Depends, HTTPException

from app.api.core.database import get_db
from app.api.models.generic.http_response import ApiResponse, ResponseType
from app.api.services.auth_service import AuthService

from ..models.schemas import User, UserLogin
from sqlalchemy.ext.asyncio import AsyncSession
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.api_route(
    "/login",
    methods = ["POST", "OPTIONS"],
    response_model = ApiResponse[User],
    summary = "Hacer login",
    responses={
        400: {"model": ApiResponse[None], "description": "Error de validación"},
        500: {"model": ApiResponse[None], "description": "Error interno"},
    }
)
async def login(
    user: UserLogin,
    db: AsyncSession = Depends(get_db)
):    
    service = AuthService(db)
    response = await service.login(user)

    if response.type == ResponseType.ERROR:
        raise HTTPException(
        status_code=response.status_code,
        detail=response.model_dump()
    )
    return response
    