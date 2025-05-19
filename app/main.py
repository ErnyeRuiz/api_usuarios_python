from fastapi import FastAPI

from app.api.routes.auth_router import auth_router
from .api.core.config import settings
from .api.routes.users_router import user_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title=settings.APP_NAME,
    description="API usuarios",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes (en producción especifica tus dominios)
    allow_credentials=True,
    allow_methods=["*"],  # O ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    allow_headers=["*"],
)

# Incluye las rutas
app.include_router(user_router)
app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de usuarios"}

@app.get("/api/data")
def read_data():
    return {"message": "CORS activo en FastAPI"}