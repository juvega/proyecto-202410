from pydantic import BaseModel
from typing import Optional

class TipoAfectacionBase(BaseModel):
    descripcion: Optional[str] = None
    nombre_afectacion: Optional[str] = None
    tipo_afectacion: Optional[str] = None

class TipoAfectacionCreate(TipoAfectacionBase):
    pass

class TipoAfectacionUpdate(TipoAfectacionBase):
    pass

class TipoAfectacion(TipoAfectacionBase):
    codigo: str

    class Config:
        orm_mode = True
