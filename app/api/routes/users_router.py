from fastapi import APIRouter, Depends, HTTPException

from app.api.core.database import get_db
from app.api.models.generic.http_response import ApiResponse, ResponseType
from app.api.services.user_service import UserService
from ..models.schemas import User
from sqlalchemy.ext.asyncio import AsyncSession
user_router = APIRouter(prefix="/users", tags=["users"])

@user_router.api_route(
    "/insertUser",
    methods = ["POST", "OPTIONS"],
    response_model = ApiResponse[int],
    summary = "Insertar usuario",
    responses={
        400: {"model": ApiResponse[None], "description": "Error de validación"},
        500: {"model": ApiResponse[None], "description": "Error interno"},
    }
)
async def insertUser(
    user: User,
    db: AsyncSession = Depends(get_db)
):    
    service = UserService(db)
    response = await service.insertUser(user)

    if response.type == ResponseType.ERROR:
        raise HTTPException(
        status_code=response.status_code,
        detail=response.model_dump()
    )
    return response
    
