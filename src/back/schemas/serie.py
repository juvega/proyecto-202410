from pydantic import BaseModel
from typing import Optional

class SerieBase(BaseModel):
    caja: Optional[int] = None
    tipo_comprobante: Optional[str] = None
    correlativo: Optional[int] = None

class SerieCreate(SerieBase):
    pass

class SerieUpdate(SerieBase):
    pass

class Serie(SerieBase):
    id: int

    class Config:
        orm_mode = True
