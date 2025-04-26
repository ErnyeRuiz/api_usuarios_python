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
    nombreusuario: str
    contrasena: str
    correo: str

    class Config:
        orm_mode = True

class User(BaseModel):
    usuarioID: int
    nombre: str
    apellidos: str
    cedula: str
    telefono: str
    fechaNacimiento: date
    fechaRegistro: datetime
    nombreUsuario: str
