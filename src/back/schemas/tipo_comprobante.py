from pydantic import BaseModel
from typing import Optional

class TipoComprobanteBase(BaseModel):
    descripcion: Optional[str] = None

class TipoComprobanteCreate(TipoComprobanteBase):
    pass

class TipoComprobanteUpdate(TipoComprobanteBase):
    pass

class TipoComprobante(TipoComprobanteBase):
    codigo: str

    class Config:
        orm_mode = True
