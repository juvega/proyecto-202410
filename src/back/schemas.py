from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

class Categoria(BaseModel):
    id: Optional[int]
    categoria: str
    fecha: datetime

    class Config:
        orm_mode = True

class Usuario(BaseModel):
    id: Optional[int]
    username: str
    password: str
    nombres: str
    apellidos: str
    admin_login: int
    fecha: datetime

    class Config:
        orm_mode = True

class Producto(BaseModel):
    id: Optional[int]
    imagen: str
    codigo: str
    descripcion: str
    categoria: int
    stock_min: int
    stock: int
    precio_compra: float
    precio_venta: float
    tipo_precio: int
    tipo_afectacion: str
    ventas: int
    unidades: str
    fecha: datetime

    class Config:
        orm_mode = True

# Puedes agregar más esquemas según sea necesario
