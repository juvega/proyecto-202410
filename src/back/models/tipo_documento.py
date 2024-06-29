from sqlalchemy import Column, String
from db import Base

class TipoDocumento(Base):
    __tablename__ = 'pos_tipo_documento'

    codigo = Column(String(3), primary_key=True, index=True)
    descripcion = Column(String(50), nullable=True)
