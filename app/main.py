from fastapi import FastAPI
from .api.core.config import settings
from .api.routes.users_router import user_router

app = FastAPI(
    title=settings.APP_NAME,
    description="API para gestión de usuarios con PostgreSQL",
    version="1.0.0"
)

# Incluye las rutas
app.include_router(user_router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de usuarios"}