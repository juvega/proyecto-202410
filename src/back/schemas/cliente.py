from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ClienteBase(BaseModel):
    tipo_documento: Optional[str] = None
    nro_documento: Optional[str] = None
    nombre_razonSocial: Optional[str] = None
    direccion: Optional[str] = None
    correo: Optional[str] = None
    celular: Optional[datetime] = None
    fecha_compra: Optional[int] = None
    monto: Optional[float] = None

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int
    fechaRegistro: datetime

    class Config:
        orm_mode = True
