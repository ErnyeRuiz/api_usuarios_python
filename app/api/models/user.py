from datetime import date
from pydantic import BaseModel, ConfigDict


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
        model_config = ConfigDict(from_attributes=True)