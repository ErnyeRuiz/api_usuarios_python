from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr

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
    nombreusuario: str
    contrasena: str
    correo: str

    class Config:
        model_config = ConfigDict(from_attributes=True)
class User(BaseModel):
    usuarioID: Optional[int] = None
    nombre: str
    apellidos: str
    cedula: str
    fechaNacimiento: date
    fechaRegistro: Optional[datetime] = None
    nombreUsuario: str
    contrasena: Optional[str] = ''
