from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class VentaBase(BaseModel):
    serie: Optional[int] = None
    fecha: Optional[date] = None
    fecha_de_pago: Optional[date] = None
    estado: Optional[str] = None
    tipo_comprobante: Optional[str] = None
    igv_gravadas: Optional[float] = None
    igv_exoneradas: Optional[float] = None
    igv_inafectas: Optional[float] = None
    metodo_pago: Optional[str] = None
    cliente: Optional[int] = None
    vendedor: Optional[int] = None

class VentaCreate(VentaBase):
    pass

class VentaUpdate(VentaBase):
    pass

class Venta(VentaBase):
    id: int
    fecha_hora: datetime

    class Config:
        orm_mode = True
