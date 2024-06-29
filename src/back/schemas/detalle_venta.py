from pydantic import BaseModel
from typing import Optional

class DetalleVentaBase(BaseModel):
    idVenta: Optional[int] = None
    idProducto: Optional[int] = None
    cantidad: Optional[int] = None
    descripcion: Optional[str] = None

class DetalleVentaCreate(DetalleVentaBase):
    pass

class DetalleVentaUpdate(DetalleVentaBase):
    pass

class DetalleVenta(DetalleVentaBase):
    id: int

    class Config:
        orm_mode = True
