from fastapi import Path
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv(override=True)  # 👈 ¡Key aquí!

class Settings(BaseSettings):
    # Configuración de la aplicación
    APP_NAME: str = os.getenv("MYSQL_APP_NAME", "Mi API FastAPI")  # Nuevo campo añadido
    
    # Configuración de la base de datos POSTGRE
    # DB_USER: str = os.getenv("DB_USER", "postgres")
    # DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    # DB_HOST: str = os.getenv("DB_HOST", "localhost")
    # DB_PORT: str = os.getenv("DB_PORT", "5432")
    # DB_NAME: str = os.getenv("DB_NAME", "mi_basedatos")

     # Configuración de la base de datos MySQL
    MYSQL_USER: str = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_HOST: str = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT: str = os.getenv("MYSQL_PORT", "3306")
    MYSQL_DATABASE: str = os.getenv("MYSQL_DB_NAME", "mi_basedatos")

     # Parámetros del pool de conexiones
    MYSQL_POOL_SIZE: int = int(os.getenv("MYSQL_POOL_SIZE", 5))
    MYSQL_MAX_OVERFLOW: int = int(os.getenv("MYSQL_MAX_OVERFLOW", 10))
    MYSQL_POOL_RECYCLE: int = int(os.getenv("MYSQL_POOL_RECYCLE", 3600))
    MYSQL_POOL_TIMEOUT: int = int(os.getenv("MYSQL_POOL_TIMEOUT", 30))

    # Configuracion del token
    SECRET_KEY: str = os.getenv("SECRET_KEY", "key")
    ALGORITHM: str = os.getenv("ALGORITHM", "algorithm")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 0)    
    
    # URL de conexión para MySQL (usando asyncmy o aiomysql como driver)
    @property
    def DATABASE_URL(self) -> str:
        return f"mysql+asyncmy://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}?charset=utf8mb4"

    # Nueva propiedad para la URL de conexión
    # @property
    # def DATABASE_URL(self) -> str:
    #     return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()