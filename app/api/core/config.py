from fastapi import Path
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    # Configuración de la aplicación
    APP_NAME: str = os.getenv("APP_NAME", "Mi API FastAPI")  # Nuevo campo añadido
    
    # Configuración de la base de datos
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    DB_NAME: str = os.getenv("DB_NAME", "mi_basedatos")

    # Configuracion del token
    SECRET_KEY: str = os.getenv("SECRET_KEY", "key")
    ALGORITHM: str = os.getenv("ALGORITHM", "algorithm")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 0)    
    
    # Nueva propiedad para la URL de conexión
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()