from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductoBase(BaseModel):
    imagen: Optional[str] = None
    codigo: Optional[str] = None
    descripcion: Optional[str] = None
    categoria: Optional[int] = None
    stock_min: Optional[int] = None
    stock: Optional[int] = None
    precio_compra: Optional[float] = None
    precio_venta: Optional[float] = None
    tipo_precio: Optional[int] = None
    tipo_afectacion: Optional[str] = None
    ventas: Optional[int] = None
    unidades: Optional[str] = None

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int
    fecha: datetime

    class Config:
        orm_mode = True
