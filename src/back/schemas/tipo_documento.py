from pydantic import BaseModel
from typing import Optional

class TipoDocumentoBase(BaseModel):
    descripcion: Optional[str] = None

class TipoDocumentoCreate(TipoDocumentoBase):
    pass

class TipoDocumentoUpdate(TipoDocumentoBase):
    pass

class TipoDocumento(TipoDocumentoBase):
    codigo: str

    class Config:
        orm_mode = True
