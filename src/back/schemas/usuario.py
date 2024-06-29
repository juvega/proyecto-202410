from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UsuarioBase(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    nombres: Optional[str] = None
    apellidos: Optional[str] = None
    email: Optional[str] = None
    admin_login: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int
    fecha: datetime

    class Config:
        orm_mode = True
