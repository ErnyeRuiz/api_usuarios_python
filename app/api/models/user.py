from datetime import date
from pydantic import BaseModel


class Usuario (BaseModel):
    usuarioid: int
    nombre: str
    apellidos: str
    cedula: str
    telefono: str
    fechanacimiento: date
    fecharegistro: date
    contrasena: str
    correo: str

    class Config:
        orm_mode = True