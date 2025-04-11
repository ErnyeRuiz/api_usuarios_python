from datetime import date, datetime
from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
    """Esquema para login"""
    username: str
    password: str

class UserInDB(BaseModel):
    """Esquema para creación/actualización y response de usuario"""
    usuarioid: int
    nombre: str
    apellidos: str
    cedula: str
    telefono: str
    fechanacimiento: date
    fecharegistro: datetime
    contrasena: str
    correo: str

    class Config:
        orm_mode = True
