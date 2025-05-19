from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from .config import settings

# # Configuración de la conexión asíncrona a PostgreSQL
# DATABASE_URL = f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

# engine = create_async_engine(DATABASE_URL, echo=True)
# AsyncSessionLocal = sessionmaker(
#     bind=engine,
#     class_=AsyncSession,
#     expire_on_commit=False
# )

# async def get_db():
#     """
#     Provee una sesión de base de datos para cada request.
#     Se cierra automáticamente al finalizar.
#     """
#     async with AsyncSessionLocal() as session:
#         yield session


# Configuración de la conexión asíncrona a MySQL
# Usando asyncmy como driver (alternativa: aiomysql)
DATABASE_MYSQL_URL = f"mysql+asyncmy://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/{settings.MYSQL_DATABASE}?charset=utf8mb4"

# Configuración del motor con parámetros específicos para MySQL
engine = create_async_engine(
    DATABASE_MYSQL_URL,
    echo=True,  # Muestra las consultas SQL (útil para desarrollo)
    pool_size=settings.MYSQL_POOL_SIZE,
    max_overflow=settings.MYSQL_MAX_OVERFLOW,
    pool_recycle=settings.MYSQL_POOL_RECYCLE,
    pool_timeout=settings.MYSQL_POOL_TIMEOUT,
    pool_pre_ping=True  # Recomendado para evitar problemas de conexión
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False
)

async def get_db():
    """
    Provee una sesión de base de datos para cada request.
    Se cierra automáticamente al finalizar.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()