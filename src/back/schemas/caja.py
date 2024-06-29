from pydantic import BaseModel
from typing import Optional

class CajaBase(BaseModel):
    nombre: Optional[str] = None
    asignacion: Optional[int] = None

class CajaCreate(CajaBase):
    pass

class CajaUpdate(CajaBase):
    pass

class Caja(CajaBase):
    id: int

    class Config:
        orm_mode = True
