from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CategoriaBase(BaseModel):
    categoria: Optional[str] = None

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    id: int
    fecha: datetime

    class Config:
        orm_mode = True
